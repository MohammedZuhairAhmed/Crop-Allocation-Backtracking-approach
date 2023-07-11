import geopandas as gpd
import matplotlib.pyplot as plt
import random

def is_valid_assignment(assignment, current_taluk, crop):
    """
    Check if assigning a crop to the current_taluk is valid,
    i.e., no neighboring taluks have the same crop.
    """
    neighbors = {
        'Athani': ['Raibag', 'Chikkodi'],
        'Raibag': ['Athani', 'Chikkodi', 'Hukkeri', 'Gokak'],
        'Chikkodi': ['Athani', 'Raibag', 'Hukkeri', 'Gokak'],
        'Hukkeri': ['Raibag', 'Chikkodi', 'Gokak', 'Belagavi'],
        'Gokak': ['Raibag', 'Chikkodi', 'Hukkeri', 'Belagavi', 'Bailhongal', 'Ramadurg', 'Savadatti'],
        'Ramadurg': ['Gokak', 'Savadatti'],
        'Savadatti': ['Ramadurg', 'Gokak', 'Bailhongal'],
        'Bailhongal': ['Savadatti', 'Gokak', 'Belagavi', 'Khanapur'],
        'Belagavi': ['Hukkeri', 'Gokak', 'Bailhongal', 'Khanapur'],
        'Khanapur': ['Belagavi', 'Bailhongal']
    }

    for taluk, assigned_crop in assignment.items():
        if taluk in neighbors[current_taluk] and assigned_crop == crop:
            return False
    return True

def backtracking_search(taluks, crops, assignment={}):
    """
    Backtracking search algorithm to assign crops to each taluk.
    """
    if len(assignment) == len(taluks):
        # All taluks have been assigned crops
        return assignment

    current_taluk = taluks[len(assignment)]
    for crop in crops:
        if is_valid_assignment(assignment, current_taluk, crop):
            assignment[current_taluk] = crop
            result = backtracking_search(taluks, crops, assignment)
            if result is not None:
                return result
            del assignment[current_taluk]

    return None

# Define the taluks and crops
taluks = [
    'Athani', 'Raibag', 'Chikkodi', 'Hukkeri', 'Gokak',
    'Ramadurg', 'Savadatti', 'Bailhongal', 'Belagavi', 'Khanapur'
]
crops = ['Jowar', 'Cotton', 'Maize', 'Paddy']

crop_colors = {
    'Jowar': 'red',
    'Cotton': 'blue',
    'Maize': 'green',
    'Paddy': 'yellow',
}

# Randomize the order of taluks and crops
random.shuffle(taluks)
random.shuffle(crops)

# Randomize the colors for the crops
all_colors = list(crop_colors.values())
random.shuffle(all_colors)
crop_colors = {crop: color for crop, color in zip(crops, all_colors)}

# Load the shapefile
shapefile_base = 'taluk_borders.shp'
taluk_borders = gpd.read_file(shapefile_base)

# Find the solution
solution = backtracking_search(taluks, crops)
print("Solution:")
for taluk, crop in solution.items():
    print(f"{taluk}: {crop}")

# Create a new figure
fig, ax = plt.subplots()

# Plot the shapefile borders
taluk_borders.plot(ax=ax)

# Loop through the taluks and plot them with assigned colors
for taluk, crop in solution.items():
    # Retrieve the taluk properties
    taluk_properties = taluk_borders[taluk_borders['KGISTalukN'] == taluk]

    if not taluk_properties.empty:
        # Get the centroid of the taluk
        centroid = taluk_properties.geometry.centroid.iloc[0]
        lat = centroid.y
        lng = centroid.x

        # Plot the taluk point
        ax.text(lng, lat, taluk, ha='center', va='center', fontsize=8)
        
        taluk_properties.plot(ax=ax, facecolor=crop_colors[crop], edgecolor='black')

# Create a legend for the crops
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10)
    for color in crop_colors.values()
]
legend_labels = list(crop_colors.keys())
ax.legend(legend_elements, legend_labels, title='Crops', loc='center left', bbox_to_anchor=(1, 0.5))

# Set the title and adjust the axes
ax.set_title('Taluk-Crop Allocation')
ax.set_aspect('equal')
ax.axis('off')

# Save the figure to a file
plt.savefig('taluk_map.png', bbox_inches='tight')
plt.close()

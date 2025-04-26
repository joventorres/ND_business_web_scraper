import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#first step: make sure to load CSV safely
file_path = "companies_total_details.csv"
df = pd.read_csv(file_path, quotechar='"', engine='python', on_bad_lines='skip')

# seocond step: Clean Data
df = df.dropna(subset=['Company Name', 'Type', 'Name'])

#step 3: Build the graph
G = nx.Graph()

for _, row in df.iterrows():
    company = row['Company Name'].strip()
    entity = row['Name'].strip()
    relation_type = row['Type'].strip()

    G.add_node(company, type='Company')
    G.add_node(entity, type='Person/Entity')
    G.add_edge(company, entity, label=relation_type)

# Step 4: Plot the graph
pos = nx.spring_layout(G, k=0.3, iterations=50)

plt.figure(figsize=(16, 16))

# Define colors for each type
edge_colors = []
for u, v, d in G.edges(data=True):
    if d['label'] == "Commercial Registered Agent":
        edge_colors.append('blue')
    elif d['label'] == "Registered Agent":
        edge_colors.append('green')
    elif d['label'] == "Owner Name":
        edge_colors.append('red')
    else:
        edge_colors.append('gray')  # fallback

# nodes drawing
nx.draw_networkx_nodes(G, pos, node_size=40, node_color="black", alpha=0.7)

# Draw edges colored by relationship type
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, alpha=0.5)

plt.title("Company - Agent/Owner Network (colored by Type)")
plt.axis('off')

#PNG save
plt.savefig("company_network_graph.png", format="png", dpi=300)
print("✅ Graph saved as 'new_company_network_graph.png'")
plt.show()

labels = ['RFI', 'Noise', 'Known Pulsars','Candidates']

rfi_total = 500
rfi_1 = 100
rfi_2 = 100
rfi_3 = 100
rfi_4 = 100
rfi_5 = 100

if rfi_total != rfi_1 + rfi_2 + rfi_3 + rfi_4 + rfi_5:
  print("RFI totals do not match")

noise_total = 500
noise_1 = 100
noise_2 = 100
noise_3 = 100
noise_4 = 100
noise_5 = 100

if noise_total != noise_1 + noise_2 + noise_3 + noise_4 + noise_5:
  print("Noise totals do not match")

known_total = 500
known_1 = 100
known_2 = 100
known_3 = 100
known_4 = 100
known_5 = 100

if known_total != known_1 + known_2 + known_3 + known_4 + known_5:
  print("Known Pulsars totals do not match")

cands_total = 500
cands_1 = 100
cands_2 = 100
cands_3 = 100
cands_4 = 100
cands_5 = 100

if cands_total != cands_1 + cands_2 + cands_3 + cands_4 + cands_5:
  print("Candidates totals do not match")


sizes = [rfi_total,noise_total, known_total, cands_total]
labels_small = ['1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5']

sizes_small = [rfi_1, rfi_2, rfi_3, rfi_4, rfi_5, noise_1, noise_2, noise_3, noise_4, noise_5, known_1, known_2, known_3, known_4,known_5, cands_1, cands_2, cands_3, cands_4, cands_5]
colors = ['#bae4bc', '#7bccc4', '#43a2ca', '#0868ac']
colors_small = ['#43a2ca', '#43a2ca', '#43a2ca', '#43a2ca', '#43a2ca' ,'#0868ac', '#0868ac', '#0868ac', '#0868ac', '#0868ac','#bae4bc', '#bae4bc', '#bae4bc','#bae4bc', '#bae4bc', '#7bccc4', '#7bccc4', '#7bccc4', '#7bccc4', '#7bccc4']

wp_big = { 'linewidth' : 2, 'edgecolor' : "white" } 
bigger = plt.pie(sizes, labels=labels, colors=colors,
                 startangle=90, wedgeprops = wp_big, frame=True)
wp_small = { 'linewidth' : 1.5, 'edgecolor' : "white" }
smaller = plt.pie(sizes_small, labels=labels_small,
                  colors=colors_small, radius=0.65,
                  startangle=90,  wedgeprops = wp_small, labeldistance=0.7, textprops = dict(color ="black"))
centre_circle = plt.Circle((0, 0), 0.3, color='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Ratings of Signal to Noise of Plots")        
plt.axis('equal')
plt.tight_layout()

plt.show()

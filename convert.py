f_in = open("books/2019.markdown")
f_out = open("2019.yml", "w")
queue = []
for line in f_in.readlines():
    if line[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        title = line.split("-")[0].split("_")[1]
        author = line.split("-")[1].strip(" ").strip("\n")
        queue.append(f"      - title: {title}\n        author: {author}\n\n")

for item in reversed(queue):
    f_out.write(item)

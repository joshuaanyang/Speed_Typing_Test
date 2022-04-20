words = "dialogue	language	rhythm a	diamond	lap abandon	diary	large	rib ability	dictate	largely ribbon able	die	laser rice abortion	diet	last rich about	differ	late	rid above	difference	lately	ride abroad	different	later	rider absence	differently	Latin	ridge absolute	difficult	latter	ridiculous absolutely	difficulty	laugh	rifle absorb	dig	laughter	right abstract	digital	launch	rim abuse	dignity	law	ring academic	dilemma	lawmaker	riot accelerate	dimension	lawn	rip accent	diminish"

w = words.replace("  ", " ")
p = w.replace(" ", ",")
words_list = [word for word in p.split(",")]

word_dict = []

words_list = [word.replace("\t", ",") for word in words_list]
words_list = [word.split(",") for word in words_list]

for x in words_list:
    for y in x:
        word_dict.append(y)


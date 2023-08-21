#dictonaries are key-value pair , spearted by commas and enclosed by curly brackets{}
dec={
    "human" : "Creature of God",
    "Eagle" : "Birds"
}
print(dec["human"])  #print the value of key human
print(dec)  # print the dictonary


print(dec["bird"])    #it through the error because bird not found
print(dec.get("bird"))  #it through the none because bird not found


print(dec.keys()) #show the keys
print(dec.values()) #show the value
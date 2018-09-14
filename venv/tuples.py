# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

title, artist, year = imelda
print(title)
print(artist)
print(year)


metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)
 
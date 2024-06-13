movies=["Rise of the Guardians","How to Train your Dragon","Inside Out","Lion King"]
search=input("Search for the movie: ").lower()
for x in movies:
    if(search==x.lower()):
            print(x,"is persent in the list!")
            break
    else:
        print(search,"not present in the list...")
        break
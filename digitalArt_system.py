from abc import ABC, abstractmethod

#========================================
# ARTIST
#=======================================
class Artist:
    def __init__(self,artist_id,name,specialization):
        self.artist_id=artist_id
        self.name=name
        self.specialization=specialization
    def display_artist(self):
        print("Artist_id:",self.artist_id)
        print("Artist_name:",self.name)
        print("Specialization:",self.specialization)

#=======================================
# ARTWORK - ABSTRACT CLASS
#======================================

class Artwork(ABC):
    def __init__(self,artwork_id,title,year,medium,artist):
        self.artwork_id=artwork_id
        self.title=title
        self.year=year
        self.medium=medium
        self.artist=artist

        self.__condition="Good"

    @abstractmethod
    def display(self):
        pass

    def get_condition(self):
        return self.__condition

    def update_condition(self, condition):
        if condition == "Good" or condition == "Damaged" or condition == "Critical" or condition == "Under Restoration" or condition == "Restored":
            self.__condition = condition
            return True
        else:
            print("Invalid condition")
            return False

#=====================================
# PAINTING
#=====================================

class Painting(Artwork):
    def __init__(self, artwork_id, title, year, medium, artist,style):
        super().__init__(artwork_id, title, year, medium, artist)
        self.style=style

    def display(self):
     print("Painting ID:",self.artwork_id)
     print("Title:",self.title)
     print("Year:",self.year)
     print("Medium:",self.medium)
     print("Artist:",self.artist.name)
     print("Style:",self.style)
     print("Condition:",self.get_condition())

#====================================
# SCULPTURE
#====================================

class Sculpture(Artwork):
    def __init__(self, artwork_id,title,year,medium,artist,material):
        super().__init__(artwork_id, title, year, medium, artist)
        self.material=material

    def display(self):
        print("Sculpture ID:",self.artwork_id)
        print("Title:",self.title)
        print("Year:",self.year)
        print("Material:",self.material)
        print("Artist:",self.artist.name)
        print("Condition:", self.get_condition())

#==================================
# DIGITAL ART
#==================================

class DigitalArt(Artwork):
    def __init__(self, artwork_id, title, year, medium, artist,file_format):
        super().__init__(artwork_id, title, year, medium, artist)
        self.file_format=file_format

    def display(self):
        print("DigitalArt ID:",self.artwork_id)
        print("Title:",self.title)
        print("Year:", self.year)
        print("File Format:",self.file_format)
        print("Artist:", self.artist.name)
        print("Condition:",self.get_condition())

#=================================
# PROVENANCE RECORD
#=================================

class ProvenanceRecord:
    def __init__(self, record_id, artwork, previous_owner, new_owner, date, transaction_type):
        self.record_id = record_id
        self.artwork = artwork
        self.previous_owner = previous_owner
        self.new_owner = new_owner
        self.date = date
        self.transaction_type = transaction_type

    def display_record(self):
        print("Record ID:",self.record_id)
        print("Artwork:",self.artwork.title)
        print("Previous Owner:",self.previous_owner)
        print("New Owner:",self.new_owner)
        print("Date:",self.date)
        print("Transaction:",self.transaction_type)

#===================================
# RESTORATION RECORD
#==================================

class RestorationRecord:
    def __init__( self,restoration_id,artwork,restorer,damage_description,technique,cost,start_date,end_date):
        self.restoration_id = restoration_id
        self.artwork = artwork
        self.restorer = restorer
        self.damage_description = damage_description
        self.technique = technique
        self.cost = cost
        self.start_date = start_date
        self.end_date = end_date

    def start_restoration(self):
        self.artwork.update_condition("Under Restoration")
        print("Restoration started.")

    def complete_restoration(self):
        self.artwork.update_condition("Restored")
        print("Restoration completed.")

    def display_restoration(self):
        print("\n--- RESTORATION RECORD ---")
        print("Restoration ID:",self.restoration_id)
        print("Artwork:",self.artwork.title)
        print("Artist:",self.artwork.artist.name)
        print("Restorer:",self.restorer)
        print("Damage:",self.damage_description)
        print("Technique:",self.technique)
        print("Cost:",self.cost)
        print("Start Date:",self.start_date)
        print("End Date:",self.end_date)
        print("Current Condition:",self.artwork.get_condition())

#======================================
# AUDIT RECORD
#=====================================

class AuditRecord:
    def __init__(self, audit_id, artwork, action, performed_by, date):
        self.audit_id = audit_id
        self.artwork = artwork
        self.action = action
        self.performed_by = performed_by
        self.date = date

    def display_audit(self):
        print("\n--- AUDIT RECORD ---")
        print("Audit ID:", self.audit_id)

        if self.artwork is not None:
            print("Artwork:", self.artwork.title)
        print("Action:", self.action)
        print("Performed By:", self.performed_by)
        print("Date:", self.date)

#====================================
# ART REPOSITORY
#====================================

class ArtRepository:
    def __init__(self):
        self.artists = []
        self.artworks = []
        self.provenance_records = []
        self.restoration_records = []
        self.audit_records = []

        self.next_restoration_id=602
        self.next_audit_id=705
        
    #====================================
    #ARTIST
    #====================================

    def add_artist(self, artist):
        self.artists.append(artist)

    def add_artist_menu(self,user):
            print("\n===== ADD ARTIST =====")
    
            artist_id = int(input("Enter Artist ID: "))

            for artist in self.artists:
                if artist.artist_id == artist_id:
                    print("Artist ID already exists!")
                    return

            name = input("Enter Artist Name: ")
            specialization = input("Enter Specialization: ")
    
            artist = Artist(artist_id, name, specialization)
    
            self.add_artist(artist)
            print("\nArtist added successfully!")

            self.create_audit(None,"Artist Added",user.name,"2026-09-06")

    def display_all_artists(self):
        print("\n=====ALL ARTIST=====")
        for artist in self.artists:
            artist.display_artist()

    #====================================
    #ARTWORK
    #====================================

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def display_all_artworks(self):
        print("\n=====ALL ARTWORKS=====")
        for artwork in self.artworks:
            artwork.display()

    def search_artwork(self, artwork_id):
        for artwork in self.artworks:
            if artwork.artwork_id == artwork_id:
                return artwork
        return None

    def search_by_title(self, title):
        for artwork in self.artworks:
            if artwork.title == title:
                return artwork
        return None

    def select_artwork(self):
        print("\n===== ARTWORKS =====")
    
        for artwork in self.artworks:
            print(artwork.artwork_id, "-", artwork.title)
    
        artwork_id = int(input("Enter Artwork ID: "))

        artwork=self.search_artwork(artwork_id)
    
        if artwork is not None:
            return artwork
                    
        print("Artwork not found!")
        return None

    #====================================
    # SEARCH ARTWORK
    #====================================

    def search_menu(self):

        print("\n===== SEARCH ARTWORK =====")
        print("1. Search by Artwork ID")
        print("2. Search by Title")

        choice = input("Enter your choice: ")
        if choice == "1":
            artwork_id = int(input("Enter Artwork ID: "))
            artwork = self.search_artwork(artwork_id)
            if artwork is not None:
                print("\n===== ARTWORK FOUND =====")
                artwork.display()
            else:
                print("Artwork not found!")
        elif choice == "2":
            title = input("Enter Artwork Title: ")
            artwork = self.search_by_title(title)
            if artwork is not None:
                print("\n===== ARTWORK FOUND =====")
                artwork.display()
            else:
                print("Artwork not found!")
        else:
             print("Invalid choice!")

    #====================================
    # ADD ARTWORK
    #====================================

    def add_artwork_menu(self,user):

        print("\n===== ADD ARTWORK =====")
        print("1. Painting")
        print("2. Sculpture")
        print("3. Digital Art")

        choice = input("Enter artwork type: ")

        artwork_id = int(input("Enter Artwork ID: "))
        for artwork in self.artworks:
            if artwork.artwork_id == artwork_id:
                print("Artwork ID already exists!")
                return
            
        title = input("Enter Title: ")
        year = input("Enter Year: ")
        medium = input("Enter Medium: ")

        print("\n===== ARTISTS =====")

        for artist in self.artists:
            print(artist.artist_id, "-", artist.name)
        artist_id = int(input("Enter Artist ID: "))
        selected_artist = None

        for artist in self.artists:
            if artist.artist_id == artist_id:
                selected_artist = artist

        if selected_artist is None:
            print("Artist not found!")
            return

        if choice == "1":
           style = input("Enter Style: ")
           artwork = Painting(artwork_id,title,year,medium,selected_artist,style)
        elif choice == "2":
            material = input("Enter Material: ")
            artwork = Sculpture(artwork_id,title,year,medium,selected_artist,material)
        elif choice == "3":
            file_format = input("Enter File Format: ")
            artwork = DigitalArt(artwork_id,title,year,medium,selected_artist,file_format)
        else:
            print("Invalid artwork type!")
            return

        self.add_artwork(artwork)
        print("\nArtwork added successfully!")

        self.create_audit(artwork,"Artwork Added",user.name,"2026-09-06")

    #====================================
    # PROVENANCE
    #====================================

    def add_provenance(self, record):
        self.provenance_records.append(record)

    def display_all_provenance(self):
        print("\n===== PROVENANCE RECORDS =====")

        for record in self.provenance_records:
            record.display_record()

    def add_provenance_menu(self,user):

        print("\n===== ADD PROVENANCE =====")
        record_id = int(input("Enter Record ID: "))
        for record in self.provenance_records:
            if record.record_id == record_id:
                print("Provenance Record ID already exists!")
                return
            
        artwork=self.select_artwork()

        if artwork is None:
            return

        previous_owner = input("Enter Previous Owner: ")
        new_owner = input("Enter New Owner: ")
        date = input("Enter Date: ")
        transaction_type = input("Enter Transaction Type: ")

        record = ProvenanceRecord(record_id,artwork,previous_owner,new_owner,date,transaction_type)

        self.add_provenance(record)
        print("\nProvenance record added successfully!")
        self.create_audit(artwork,"Provenance Added",user.name,date)

    #====================================
    # RESTORATION
    #====================================

    def add_restoration(self, restoration):
        self.restoration_records.append(restoration)

    def create_restoration(self, artwork, restorer, damage_description,technique, cost, start_date, end_date):

        restoration = RestorationRecord(self.next_restoration_id,artwork,restorer,damage_description,technique,cost,start_date,end_date)
        self.add_restoration(restoration)
        self.next_restoration_id=self.next_restoration_id+1
        return restoration

    def display_all_restorations(self):
        print("\n===== RESTORATION RECORDS =====")

        for restoration in self.restoration_records:
            restoration.display_restoration()

    #====================================
    # AUDIT
    #====================================

    def add_audit(self, audit):
        self.audit_records.append(audit)

    def create_audit(self, artwork, action, performed_by, date):
        audit = AuditRecord(self.next_audit_id,artwork,action,performed_by,date)
        self.add_audit(audit)
        self.next_audit_id=self.next_audit_id + 1
        print("Audit record created successfully.")

    def display_all_audits(self):

        print("\n===== AUDIT TRAIL =====")
        for audit in self.audit_records:
            audit.display_audit()

#====================================
# USER - ABSTRACT CLASS
#====================================

class User(ABC):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    @abstractmethod
    def show_role(self):
        pass

    @abstractmethod
    def show_menu(self):
        pass

#====================================
# ARTIST USER
#====================================

class ArtistUser(User):
    def show_role(self):
        print("Role: Artist")

    def show_menu(self):
        print("\n===== ARTIST MENU =====")
        print("1. View Artworks")
        print("2. View Provenance")
        print("3. Logout")

#====================================
# CURATOR
#====================================

class Curator(User):
    def show_role(self):
        print("Role: Curator")

    def show_menu(self):
        print("\n===== CURATOR MENU =====")
        print("1. View Artworks")
        print("2. Add Artwork")
        print("3. Add Provenance")
        print("4. View Provenance")
        print("5. Logout")

#====================================
# RESTORER
#====================================

class Restorer(User):
    def show_role(self):
        print("Role: Restorer")

    def show_menu(self):
        print("\n===== RESTORER MENU =====")
        print("1. View Artworks")
        print("2. Start Restoration")
        print("3. Complete Restoration")
        print("4. Update Condition")
        print("5. Logout")

#====================================
# ADMINISTRATOR
#====================================

class Administrator(User):
    def show_role(self):
        print("Role: Administrator")

    def show_menu(self):
        print("\n===== ADMINISTRATOR MENU =====")
        print("1. View Artists")
        print("2. Add Artist")
        print("3. View Artworks")
        print("4. Search Artwork")
        print("5. Add Artwork")
        print("6. Add Provenance")
        print("7. View Provenance")
        print("8. View Restoration")
        print("9. View Audit Trail")
        print("10. Logout")

#====================================
# INITIAL DATA
#====================================

artist1=Artist(201,"meera rao","water color")
artist2=Artist(202,"Arjun singh","digital art")

Painting1=Painting(301,"Indian sunset","2020","water color",artist1,"Contemporary")

Sculpture1=Sculpture(302,"The Thinker",2005,"Bronze",artist2,"Bronze")

DigitalArt1=DigitalArt(303,"Future world","2025","Digital",artist2,"PNG")

#====================================
#PROVENANCE INITIAL DATA
#====================================

record1=ProvenanceRecord(501,Painting1,"Meera Rao","Ravi Kumar","2022-06-15","Sale")
record2=ProvenanceRecord(502,Painting1,"Ravi Kumar","City Art Gallery","2024-03-20","Donation")
record3=ProvenanceRecord(503,Painting1,"City Art Gallery","National Museum","2026-01-10","Transfer")

#====================================
#RESTORATION INITIAL DATA
#====================================

restoration1 = RestorationRecord(601,Painting1,"Ananya Sharma","Color fading and surface damage","Color reconstruction",15000,"2026-02-10","2026-02-25")
restoration2 = RestorationRecord( 602, DigitalArt1, "Ananya Sharma", "Damage found during inspection", "Professional restoration", 15000, "2026-09-06", "2026-09-26" )
#====================================
#AUDIT INITIAL DATA
#====================================

audit1=AuditRecord(701,Painting1,"Artwork Registered","Museum Administrator","2020-05-10")
audit2=AuditRecord(702, Painting1,"Ownership Transferred","Museum Administrator","2026-01-10")
audit3=AuditRecord(703,Painting1,"Restoration Started","Ananya Sharma","2026-02-10")
audit4=AuditRecord(704,Painting1,"Restoration Completed","Ananya Sharma","2026-02-25")

Painting1.update_condition("Damaged")

#====================================
#REPOSITORY
#====================================

repository = ArtRepository()

repository.add_artist(artist1)
repository.add_artist(artist2)

repository.add_artwork(Painting1)
repository.add_artwork(Sculpture1)
repository.add_artwork(DigitalArt1)

repository.add_provenance(record1)
repository.add_provenance(record2)
repository.add_provenance(record3)

repository.add_restoration(restoration1)
repository.add_restoration(restoration2)

repository.add_audit(audit1)
repository.add_audit(audit2)
repository.add_audit(audit3)
repository.add_audit(audit4)

#====================================
#USERS
#====================================

artist_user = ArtistUser(801,"Meera Rao")
curator_user = Curator(802,"Ravi Kumar")
restorer_user = Restorer(803,"Ananya Sharma")
admin_user = Administrator(804,"Museum Administrator")

users = [artist_user,curator_user,restorer_user,admin_user]

#====================================
# LOGIN
#====================================

def login(users):
    user_id = int(input("Enter User ID: "))
    for user in users:
        if user.user_id == user_id:
            print("\nLogin Successful!")
            print("Welcome:", user.name)
            user.show_role()
            return user
    print("Invalid User ID!")
    return None

# ==========================================
# MAIN APPLICATION
# ==========================================

while True:
    current_user = login(users)
    if current_user is None:
        print("Login failed!")
        continue
    while True:
        current_user.show_menu()
        choice = input("Enter your choice: ")

        # ==============================
        # ARTIST
        # ==============================

        if isinstance(current_user, ArtistUser):
            if choice == "1":
                repository.display_all_artworks()
            elif choice == "2":
                repository.display_all_provenance()
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice!")

        # ==============================
        # CURATOR
        # ==============================

        elif isinstance(current_user, Curator):
            if choice == "1":
                repository.display_all_artworks()
            elif choice == "2":
                repository.add_artwork_menu(current_user)
            elif choice == "3":
                repository.add_provenance_menu(current_user)
            elif choice == "4":
                repository.display_all_provenance()
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice!")

        # ==============================
        # RESTORER
        # ==============================

        elif isinstance(current_user, Restorer):
            if choice == "1":
                repository.display_all_artworks()
            elif choice == "2":
               artwork = repository.select_artwork()
               if artwork is not None:
                   restoration = None
                   for record in repository.restoration_records:
                       if record.artwork == artwork:
                           restoration = record
                           break
                   if restoration is not None:
                      if artwork.get_condition() == "Under Restoration":
                          print("Restoration is already under restoration.")
                      elif artwork.get_condition() == "Restored":
                          print("Artwork is already restored.")
                      else:
                          restoration.start_restoration()
                          date=input("Enter start date:")
                          repository.create_audit(artwork,"Restoration Started",current_user.name,date)
               else:
                    print("No restoration record found for this artwork.")
            elif choice == "3":
                artwork=repository.select_artwork()
                if artwork is not None:
                    restoration=None
                    for record in repository.restoration_records:
                        if record.artwork==artwork:
                            restoration=record
                            break
                    if restoration is not None:
                        if artwork.get_condition()=="Under Restoration":
                            restoration.complete_restoration()
                            date=input("Enter completion date:")
                            repository.create_audit(artwork,"Restoration Completed",current_user.name,date)
                        elif artwork.get_condition()=="Restored":
                            print("Artwork is already restored.")
                        else:
                            print("Restoration has not been started")
                    else:
                        print("No restoration record found for this artwork")
            elif choice == "4":
                artwork=repository.select_artwork()
                if artwork is not None:
                    condition=input("Enter new condition:")
                    updated=artwork.update_condition(condition)

                    if updated:
                        print("Condition updated successfully.")
                        print("Current Condition:",artwork.get_condition())
                        date=input("Enter date:")
                        repository.create_audit(artwork,"Condition Updated",current_user.name,date)
                    else:
                        print("Condition was not updated.")
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice!")

        # ==============================
        # ADMINISTRATOR
        # ==============================

        elif isinstance(current_user, Administrator):

            if choice == "1":
                repository.display_all_artists()
            elif choice == "2":
                repository.add_artist_menu(current_user)
            elif choice == "3":
                repository.display_all_artworks()
            elif choice == "4":
                repository.search_menu()
            elif choice == "5":
                repository.add_artwork_menu(current_user)
            elif choice == "6":
                repository.add_provenance_menu(current_user)
            elif choice == "7":
                repository.display_all_provenance()
            elif choice == "8":
                repository.display_all_restorations()
            elif choice == "9":
                repository.display_all_audits()
            elif choice == "10":
                print("Logging out...")
                break
            else:
                print("Invalid choice!")
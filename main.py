from planet import Planet
from lab import Lab

def main():
    print("=== Alien Plant Hybridization Simulator ===")
    researcher = input("Enter your researcher name: ").strip() or "Alien"
    print(f"\nWelcome, Dr. {researcher}! You have been dispatched to study extraterrestrial flora\n")
    
    p = Planet()
    lab = Lab()
    lab.set_base_plants(p.plants)
    
    day = 1
    should_print_header = True
    
    while True:
        if should_print_header:
            print(f"\n=== Day {day} ===")
            print(f"Researcher: Dr. {researcher}")
            print(f"Current Temp: {p.temp}°C | Radiation: {p.rad}/5")
            print(f"Lab Energy: {lab.energy} | Species Discovered: {len(lab.discovered)}")
            should_print_header = False
        
        print("\n1. Explore Terrain")
        print("2. Analyze Sample")
        print("3. Breed Hybrid")
        print("4. View Catalog")
        print("5. End Mission")
        
        try:
            choice = input("Select action: ")
            
            if choice == "1":
                found = p.explore()
                if found:
                    lab.add_sample(found)
                day += 1
                should_print_header = True
            elif choice == "2":
                lab.analyze()
            elif choice == "3":
                success = lab.breed_plant()
                if success:
                    day += 1
                    should_print_header = True
            elif choice == "4":
                lab.show_plants()
            elif choice == "5":
                natural = len([p for p in lab.discovered if not p['dna'].startswith('HY')])
                hybrids = len([p for p in lab.discovered if p['dna'].startswith('HY')])
                print(f"\nMission complete!")
                print(f"Discovered {natural} natural species")
                print(f"Created {hybrids} hybrid species")
                print(f"Total research days: {day-1}")
                break
            else:
                print("Invalid input")
                
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

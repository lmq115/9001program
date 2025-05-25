import random

class Lab:
    def __init__(self):
        self.energy = 50
        self.samples = []
        self.discovered = []
        self.hybrid_id = 1
        self.base_plants = None
    
    def set_base_plants(self, plants_dict):
        self.base_plants = plants_dict
    
    def add_sample(self, plant):
        if not any(p['dna'] == plant['dna'] for p in self.discovered):
            self.discovered.append(plant)
            print(f"New species recorded: {plant['name']}")
        self.samples.append(plant)
    
    def analyze(self):
        if not self.samples:
            print("No samples to analyze")
            return
        
        print("\nAvailable samples:")
        for i, p in enumerate(self.samples, 1):
            print(f"{i}. {p['name']} (DNA: {p['dna']})")
        
        try:
            idx = int(input("Select sample: "))-1
            if 0 <= idx < len(self.samples):
                p = self.samples[idx]
                print(f"\n{p['name']} Analysis:")
                print(f"Optimal Temp: {p['temp']}°C")
                print(f"Rad Resistance: {p['rad']}/5")
                print(f"Origin: {p['terrain']}")
                self.energy -= 5
            else:
                print("Invalid selection")
        except ValueError:
            print("Please enter a valid number")
    
    def breed_plant(self):
        if len(self.samples) < 2:
            print("Need at least 2 samples")
            return False
        
        if self.energy < 20:
            print("Not enough energy (needs 20)")
            return False
        
        print("\nSelect two plants to breed:")
        for i, p in enumerate(self.samples, 1):
            print(f"{i}. {p['name']} (DNA: {p['dna']})")
        
        try:
            a, b = map(int, input("Enter two numbers (e.g. '1 2'): ").split())
            a -= 1
            b -= 1
            
            if not (0 <= a < len(self.samples) and 0 <= b < len(self.samples)):
                print("Invalid selection")
                return False
            
            p1, p2 = self.samples[a], self.samples[b]
            new_name = f"{random.choice([p1['attribute'], p2['attribute']])} " \
                       f"{random.choice([p1['type'], p2['type']])}"
            
            new_dna = f"HY{self.hybrid_id}"
            self.hybrid_id += 1
            
            new_plant = {
                'name': new_name,
                'dna': new_dna,
                'rad': (p1['rad'] + p2['rad']) // 2 + random.randint(-1, 1),
                'temp': (p1['temp'] + p2['temp']) // 2 + random.randint(-5, 5),
                'terrain': self._determine_terrain(p1, p2),
                'attribute': new_name.split()[0],
                'type': new_name.split()[1]
            }
            
            print(f"\nSuccessfully created: {new_name} (DNA: {new_dna})")
            print(f"Properties: Temp {new_plant['temp']}°C | Rad {new_plant['rad']}/5")
            print(f"Habitat: {new_plant['terrain']}")
            
            self.discovered.append(new_plant)
            self.samples.append(new_plant)
            self.energy -= 20
            return True
            
        except (ValueError, IndexError):
            print("Invalid input")
            return False
    
    def _determine_terrain(self, p1, p2):
        terrains = [p1['terrain'], p2['terrain']]
        return random.choice(terrains)
    
    def show_plants(self):
        if not self.discovered:
            print("No plants discovered yet")
            return
        
        print("\n=== Plant Catalog ===")
        for p in sorted(self.discovered, key=lambda x: x['dna']):
            prefix = "BASE" if not p['dna'].startswith('HY') else "HYBRID"
            print(f"[{prefix}] {p['dna']}: {p['name']}")
            print(f"    Temp: {p['temp']}°C | Rad: {p['rad']}/5 | Origin: {p['terrain']}")

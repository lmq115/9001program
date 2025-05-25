import random

class Planet:
    def __init__(self):
        self.temp = random.randint(-20, 50)
        self.rad = random.randint(1, 5)
        self.terrains = [
            "Crystal Plains", "Acid Swamp", "Metal Forest",
            "Gas Hills", "Quantum Valley", "Lava Lakes", 
            "Electro Fields", "Antimatter Desert"
        ]
        
        self.terrain_attributes = {
            "Crystal Plains": ["Shining", "Prism", "Crystalline"],
            "Acid Swamp": ["Acidic", "Toxic", "Corrosive"],
            "Metal Forest": ["Iron", "Magnetic", "Alloy"],
            "Gas Hills": ["Misty", "Gaseous", "Helium"],
            "Quantum Valley": ["Superposed", "Entangled", "Probabilistic"],
            "Lava Lakes": ["Fiery", "Magma", "Thermal"],
            "Electro Fields": ["Conductive", "Polarized", "Electric"],
            "Antimatter Desert": ["Dark", "Negative", "Annihilating"]
        }
        
        self.plant_types = {
            "Crystal Plains": ["Grass", "Flower", "Vine"],
            "Acid Swamp": ["Vine", "Mushroom", "Algae"],
            "Metal Forest": ["Tree", "Fern", "Moss"],
            "Gas Hills": ["Algae", "Grass", "Flower"],
            "Quantum Valley": ["Fern", "Vine", "Berry"],
            "Lava Lakes": ["Grass", "Willow", "Moss"],
            "Electro Fields": ["Grass", "Flower", "Berry"],
            "Antimatter Desert": ["Cactus", "Grass", "Vine"]
        }
        
        self.plants = self._init_plants()
    
    def _init_plants(self):
        plants = {}
        for terrain in self.terrains:
            plants[terrain] = []
            for i in range(3):
                dna = f"{terrain[:2].upper()}{i+1}"
                name = f"{self.terrain_attributes[terrain][i]} {self.plant_types[terrain][i]}"
                plants[terrain].append({
                    'name': name,
                    'dna': dna,
                    'rad': self._get_rad_for_terrain(terrain),
                    'temp': self._get_base_temp(terrain),
                    'terrain': terrain,
                    'attribute': self.terrain_attributes[terrain][i],
                    'type': self.plant_types[terrain][i]
                })
        return plants
    
    def _get_base_temp(self, terrain):
        temp_ranges = {
            "Crystal Plains": (5, 25),
            "Acid Swamp": (25, 40),
            "Metal Forest": (10, 30),
            "Gas Hills": (-10, 10),
            "Quantum Valley": (20, 40),
            "Lava Lakes": (60, 100),
            "Electro Fields": (15, 35),
            "Antimatter Desert": (40, 60)
        }
        return random.randint(*temp_ranges[terrain])
    
    def _get_rad_for_terrain(self, terrain):
        return {
            "Crystal Plains": 2,
            "Acid Swamp": 4,
            "Metal Forest": 2,
            "Gas Hills": 3,
            "Quantum Valley": 5,
            "Lava Lakes": 4,
            "Electro Fields": 3,
            "Antimatter Desert": 5
        }[terrain]
    
    def explore(self):
        terrain = random.choice(self.terrains)
        print(f"\nExploring {terrain}...")
        
        success_chance = 0.6 - (self.rad * 0.05)
        if random.random() < max(0.3, success_chance):
            plant = random.choice(self.plants[terrain])
            print(f"Discovered: {plant['name']} (DNA: {plant['dna']})")
            return plant
        print("No new species found this time")
        return None
    
    def change_weather(self):
        self.temp += random.randint(-5, 5)
        self.rad = random.randint(1, 5)
        print(f"Weather changed: Temp now {self.temp}°C, Radiation {self.rad}/5")

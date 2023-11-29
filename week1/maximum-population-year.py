class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        min_year = float('inf')  # To find the minimum birth year
        max_year = float('-inf')  # To find the maximum death year
    
    # Find the minimum birth year and maximum death year
        for birth, death in logs:
            min_year = min(min_year, birth)
            max_year = max(max_year, death - 1)
    
        max_population = 0
        max_population_year = None
    
    # Iterate through each year and count the population
        for year in range(min_year, max_year + 1):
            population = 0
            for birth, death in logs:
                if birth <= year <= death - 1:
                    population += 1
            if population > max_population:
                max_population = population
                max_population_year = year
    
        return max_population_year
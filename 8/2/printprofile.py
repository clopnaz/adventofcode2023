import pstats
stats = pstats.Stats('main.profile') 
stats.sort_stats('tottime').print_stats()

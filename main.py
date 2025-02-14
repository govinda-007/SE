import pandas                        as pd
from core import methods             as m1
from core import HelperTools         as ht

from config import pdict
import os

# -----------------------------------------------------------------------------
@ht.timer
def main():
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""

    df_geodat_plz = pd.read_csv(os.path.join(os.getcwd(), 'datasets', 'geodata_berlin_plz.csv'), delimiter=';')  
    
    df_lstat = df_lstat = pd.read_csv(os.path.join(os.getcwd(), 'datasets', 'Ladesaeulenregister.csv'), delimiter=';',low_memory=False)
    df_lstat2  =  m1.preprop_lstat(df_lstat, df_geodat_plz, pdict)
    gdf_lstat3 = m1.count_plz_occurrences(df_lstat2)
    
    df_residents = pd.read_csv(os.path.join(os.getcwd(), 'datasets', 'plz_einwohner.csv'), delimiter=',')
    gdf_residents2 = m1.preprop_resid(df_residents, df_geodat_plz, pdict)

    ## Run the application creator
    m1.make_streamlit_electric_Charging_resid(gdf_lstat3, gdf_residents2)

    ## for analysis
    gdf_joined = gdf_lstat3.merge(gdf_residents2, on='PLZ', how='left')
    gdf_joined=gdf_joined[['PLZ','Number','Einwohner']]
    demand_for_electric_stations=gdf_joined[(gdf_joined['Einwohner']>15000) & (gdf_joined['Number']<10)]
    print(demand_for_electric_stations)
# -----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__": 
    main()


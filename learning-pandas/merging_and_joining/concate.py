import pandas as pd

df_region1 = pd.DataFrame({
    "Employee": ["Aayu", "Riya", "Shrey"],  
    "Region": ["North", "South", "East"]
})


df_region2 = pd.DataFrame({
    "Employee": ["Anurag", "Bharat", "Aanchal"],    
    "Region": ["West", "North", "South"]
})

# con_ver = pd.concat([df_region1, df_region2], ignore_index=True)
# print(con_ver)


con_hor = pd.concat([df_region1, df_region2], axis =1, ignore_index=True)
print(con_hor)
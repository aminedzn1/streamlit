
accomplished = obj_data[obj_data.columns[8:]]

array_accomplished = accomplished.to_numpy().flatten()
array_accomplished = array_accomplished[array_accomplished.astype(str) != '<NA>']
st.write(f"{array_accomplished.astype(int).mean()*100}%")
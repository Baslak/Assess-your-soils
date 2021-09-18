from database import sql_select, sql_write

def vineyard_check(owner_email):
  vineyard_info = sql_select("SELECT id, owner_email, vineyard_site, vineyard_size, varieties, elevation, orientation, E_L_Stage FROM vineyard WHERE owner_email = %s ORDER BY vineyard_size DESC", [owner_email])
  print(vineyard_info)
  
  if len(vineyard_info) == 0:
    return None
  else:
    vineyard_info = vineyard_info[0]
    vineyard = {
        'id': vineyard_info[0],
        'owner_email': vineyard_info[1],
        'vineyard_site': vineyard_info[2],
        'vineyard_size': vineyard_info[3],
        'varieties': vineyard_info[4],
        'elevation': vineyard_info[5],
        'orientation': vineyard_info[6],
        'E_L_Stage': vineyard_info[7]
    }
    return vineyard

def amend_vineyard(id):
  vineyard_info = sql_select("SELECT id, owner_email, vineyard_site, vineyard_size, varieties, orientation, elevation, E_L_Stage from vineyard WHERE id = %s", [id])

  if len(vineyard_info) == 0:
    return None
  else:
    vineyard_info = vineyard_info[0]
    print(vineyard_info)
    vineyard = {
        'id': vineyard_info[0],
        'owner_email': vineyard_info[1],
        'vineyard_site': vineyard_info[2],
        'vineyard_size': vineyard_info[3],
        'varieties': vineyard_info[4],
        'orientation': vineyard_info[5],
        'elevation': vineyard_info[6],
        'E_L_stage': vineyard_info[7],
    }
    return vineyard

def add_vineyard(owner_email, vineyard_site, vineyard_size, varieties, orientation, elevation, E_L_stage):
  sql_write("INSERT INTO vineyard (owner_email, vineyard_site, vineyard_size, varieties, orientation, elevation, E_L_stage) VALUES (%s, %s, %s, %s, %s, %s, %s)", [owner_email, vineyard_site, vineyard_size, varieties, orientation, elevation, E_L_stage])

def delete_vineyard(id):
  sql_write("DELETE from vineyard WHERE id = %s", [id])

def update_vineyard(vineyard_site, vineyard_size, varieties, elevation, orientation, E_L_Stage, id):
  sql_write("UPDATE vineyard SET vineyard_site=%s, vineyard_size=%s, varieties=%s, elevation=%s, orientation=%s, E_L_Stage=%s WHERE id = %s", [vineyard_site, vineyard_size, varieties, elevation, orientation, E_L_Stage, id])
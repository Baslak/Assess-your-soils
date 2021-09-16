from database import sql_select, sql_write

def login_check(user_id):
  user_info = sql_select("SELECT id, full_name, company, email, password_hash FROM users WHERE id = %s", [user_id])
  print(user_info)
  
  if len(user_info) == 0:
    return None
  
  user_info = user_info[0]
  user = {
    'id': user_info[0],
    'full_name': user_info[1],
    'company': user_info[2],
    'email': user_info[3],
    'password_hash': user_info[4],
  }
  return user


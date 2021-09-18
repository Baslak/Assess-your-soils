from database import sql_select, sql_write

def check_spray(el):
    spray_info = sql_select("SELECT vine_stage, e_l, product, pd_target, notes, rate_per_ha, rate_per_100l, cf, water_rate, approx_timing FROM spray_program WHERE e_l = %s", [el])
    print(spray_info)
  
    if len(spray_info) == 0:
        return None
    
    spray_info = spray_info[0]
    spray = {
        'vine_stage': spray_info[0],
        'e_l': spray_info[1],
        'product': spray_info[2],
        'pd_target': spray_info[3],
        'notes': spray_info[4],
        'rate_per_ha': spray_info[5],
        'rate_per_100l': spray_info[6],
        'cf': spray_info[7],
        'water_rate': spray_info[8],
        'approx_timing': spray_info[9],
    }
    return spray

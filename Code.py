def water_Q(cement_weight_A,fly_ash_weight_B,silica_fume_weight_C,other_weight_D,WC_ratio_E):
    water_Q = (cement_weight_A + fly_ash_weight_B + silica_fume_weight_C + other_weight_D)*WC_ratio_E
    return water_Q

def volume_R(cement_weight_A,sg_cement_J):
    volume_R = cement_weight_A/(sg_cement_J*62.4)
    return volume_R

def calc_fly_ash_S(fly_ash_weight_B,sg_fly_ash_K):
    calc_fly_ash_S = fly_ash_weight_B/(sg_fly_ash_K*62.4) 
    return calc_fly_ash_S

def calc_silica_fume_T(silica_fume_weight_C,sg_silica_fume_L):
    calc_silica_fume_T = silica_fume_weight_C/(sg_silica_fume_L*62.4)
    return calc_silica_fume_T

def calc_other_SCM_U(other_weight_D,sg_other_SCM_M):
    calc_silica_fume_T = other_weight_D/(sg_other_SCM_M*62.4)
    return calc_silica_fume_T

def air_volume_V(air_content_F):
    air_volume_V = (air_content_F/100)*27
    return air_volume_V

def water_volume_W(water_Q):
    water_volume_W = water_Q/62.4
    return water_volume_W

def total_agg_vol_X(volume_R, calc_fly_ash_S, calc_silica_fume_T, calc_other_SCM_U, air_volume_V, water_volume_W):
    total_agg_vol_X = 27 - volume_R - calc_fly_ash_S - calc_silica_fume_T - calc_other_SCM_U - air_volume_V - water_volume_W
    return total_agg_vol_X

def calc_fine_agg_Y(percent_fine_G, sg_fine_N, total_agg_vol_X):
    calc_fine_agg_Y = 62.4 * (percent_fine_G/100) * sg_fine_N * total_agg_vol_X
    return calc_fine_agg_Y

def calc_coarse_agg_Z(percent_coarse_H, sg_coarse_O, total_agg_vol_X):
    calc_fine_agg_Y = 62.4 * (percent_coarse_H/100) * sg_coarse_O * total_agg_vol_X
    return calc_fine_agg_Y

def calc_other_agg_AA(percent_other_I, sg_other_P, total_agg_vol_X):
    calc_fine_agg_Y = 62.4 * (percent_other_I/100) * sg_other_P * total_agg_vol_X
    return calc_fine_agg_Y

project_no = int(input("Enter project number: ")) 
concrete_class = input("Enter class of concrete: ")
cement_weight_A = float(input("Enter Cement Weight A in lb/yd^3: "))
fly_ash_weight_B = float(input("Enter Fly Ash Weight B in lb/yd^3: "))
silica_fume_weight_C = float(input("Enter Silica Fum Weight C in lb/yd^3: ")) 
other_weight_D = float(input("Enter Other SCM Weight D in lb/yd^3: "))
WC_ratio_E = float(input("Enter Water Cement Ratio E in lb/yd^3: "))
air_content_F = float(input("Enter target air content F (%): "))
percent_fine_G = float(input("Enter percent fine aggregate G (%): "))
percent_coarse_H = float(input("Enter percent coarse aggregate H (%): "))
percent_other_I = float(input("Enter percent other aggregate I (%): "))
sg_cement_J = float(input("Enter Specific Gravity of Cement J in lb/yd^3: "))
sg_fly_ash_K = float(input("Enter Specific Gravity of Fly Ash K in lb/yd^3: "))
sg_silica_fume_L = float(input("Enter Specific Gravity of Silica Fume L in lb/yd^3: "))
sg_other_SCM_M = float(input("Enter Specific Gravity of other SCM M in lb/yd^3: "))
sg_fine_N = float(input("Enter specific gravity of fine aggregate N: "))
sg_coarse_O = float(input("Enter specific gravity of coarse aggregate O: "))
sg_other_P = float(input("Enter specific gravity of other aggregate P: "))

water_Q = (cement_weight_A + fly_ash_weight_B + silica_fume_weight_C + other_weight_D)*WC_ratio_E

R = volume_R(cement_weight_A,sg_cement_J)
S = calc_fly_ash_S(fly_ash_weight_B,sg_fly_ash_K)
T = calc_silica_fume_T(silica_fume_weight_C,sg_silica_fume_L)
U = calc_other_SCM_U(other_weight_D,sg_other_SCM_M)

V = air_volume_V(air_content_F)
W = water_volume_W(water_Q)

X = total_agg_vol_X(R,S,T,U,V,W)

Y = calc_fine_agg_Y(percent_fine_G, sg_fine_N, X)
Z = calc_coarse_agg_Z(percent_coarse_H, sg_coarse_O, X)
AA = calc_other_agg_AA(percent_other_I, sg_other_P, X)
# Output: Final Weight Chart

print("\n---------------------------------------------")
print(" NDOT Concrete Mix Design – Weight Summary")
print("         (1 Cubic Yard of Concrete)")
print("---------------------------------------------")
print(f"Project Number:       {project_no}")
print(f"Class of Concrete:    {concrete_class}")
print("---------------------------------------------")
print(f"Cement (A):            {cement_weight_A:8.1f} lb")
print(f"Fly Ash (B):           {fly_ash_weight_B:8.1f} lb")
print(f"Silica Fume (C):       {silica_fume_weight_C:8.1f} lb")
print(f"Other SCM (D):         {other_weight_D:8.1f} lb")
print("---------------------------------------------")
print(f"Fine Aggregate (Y):    {Y:8.0f} lb")
print(f"Coarse Aggregate (Z):  {Z:8.0f} lb")
print(f"Other Aggregate (AA):  {AA:8.0f} lb")
print("---------------------------------------------")
print(f"Water (Q):             {water_Q:8.0f} lb")
print("---------------------------------------------")
print("End of Mix Design Summary")
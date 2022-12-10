viewing_d<- 186
stim_size<- 100
rad_to_deg<- function(rad) (rad * 180) / (pi)
angular_subtense<- 2*rad_to_deg(atan(0.5*stim_size/viewing_d))

cpd<- seq(from = 0.05, to = 0.4, by =0.05)
cpp<- cpd / 4000

deg_p_cm<- angular_subtense / (stim_size/10)
cpcm<- cpd / deg_p_cm

# we need the cycles per degree for pythons psychotoolbox 

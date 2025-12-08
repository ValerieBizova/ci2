// ============================================
// etoh6.pov
// Six ethanol molecules arranged in a hexagon
// ============================================

#include "babel_povray3.inc"
#include "etoh.pov"  // contains the molecule definition mol_0

// Camera
camera {
    location <0, 0, -30>
    look_at <0, 0, 0>
}

// Lighting
light_source {
    <20, 20, -20>
    color rgb 1
}

background { color rgb <1,1,1> }

// Hexagon placement
#declare R = 12;  // radius of hexagon
#declare N = 6;   // number of molecules

#for (I, 0, N-1)
    #declare Angle = I * 360 / N;  // degrees

    object {
        mol_0
        rotate <0, 0, Angle>
        translate <R * cos(radians(Angle)), R * sin(radians(Angle)), 0>
    }
#end

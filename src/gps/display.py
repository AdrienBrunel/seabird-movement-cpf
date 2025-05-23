# ======================================================= #
# LIBRARIES
# ======================================================= #
from src import utils


# ======================================================= #
# DISPLAY [GPS METHODS]
# ======================================================= #
def display_data_summary(self):
                
    # compute distance between first position and the estimated nest position    
    pos0 = [self.df.loc[0,"longitude"], self.df.loc[0,"latitude"]]
    nest = self.nest_position
    d_pos0_nest = utils.ortho_distance(nest[0], nest[1], pos0[0], pos0[1])

    # store information
    print("# ============================== SUMMARY ============================== #")
    print("# ------------------------------ METADATA ----------------------------- #")
    print("# + Group = %s" % self.group)
    print("# + Id    = %s" % self.id)
    print("# ------------------------------ DATA --------------------------------- #")
    print("# + Nb of measures       = %d" % self.n_df)
    print("# + Date range           = %s | %s" % (self.start_datetime, self.end_datetime))       
    print("# + Nb of trips          = %d" % self.n_trip) 
    print("# + Time resolution      = %.1f s" % self.resolution)
    print("# + Total duration       = %.2f days" % self.total_duration)
    print("# + Total length         = %.1f km" % self.total_length)
    print("# + Max distance to nest = %.1f km" % self.dmax)
    if self.n_trip>0:
        print("# ------------------------------ TRIP --------------------------------- #")
        print("# + Longest trip         = %.1f h" % self.trip_statistics["duration"].max())
        print("# + Median trip duration = %.1f h" % self.trip_statistics["duration"].quantile(0.5))
        print("# + Largest trip         = %.1f km" % self.trip_statistics["length"].max())
        print("# + Median trip length   = %.1f km" % self.trip_statistics["length"].quantile(0.5))
    print("# + First position (%.5f, %.5f) is %.3fkm away from the estimated nest position (%.5f, %.5f)" % (pos0[0], pos0[1], d_pos0_nest, nest[0], nest[1]))
    print("# ===================================================================== #")
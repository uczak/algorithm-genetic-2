class Individual(object):
    def __init__(self, term_x=0, term_y=0,term_w=0, term_z=0, chromosome=0, fun=0, weighting=0):
        self.__term_x = str(term_x).rjust(2, '0')
        self.__term_y = str(term_y).rjust(2, '0')
        self.__term_w = str(term_w).rjust(2, '0')
        self.__term_z = str(term_z).rjust(2, '0')
        self.__chromosome = chromosome
        self.__fun = fun
        self.__weighting = weighting

    def print_not_weighting(self):
        return "%s %s %s %s %s %s" % (self.__term_x, self.__term_y, self.__term_w, self.__term_z, self.__chromosome, self.__fun)

    def print_yes_weighting(self):
        return "%s %s %s %s %s %s %s" % (self.__term_x, self.__term_y, self.__term_w, self.__term_z, self.__chromosome, self.__fun, self.__weighting)

    def get_term_x(self):
        return self.__term_x

    def get_term_y(self):
        return self.__term_y
    
    def get_term_w(self):
        return self.__term_w

    def get_term_z(self):
        return self.__term_z

    def get_chromosome(self):
        return self.__chromosome
    
    def set_chromosome(self, chromosome):
        self.__chromosome = chromosome

    def get_fun(self):
        return self.__fun

    def set_fun(self, fun):
        self.__fun = fun

    def get_weighting(self):
        return self.__weighting

    def set_weighting(self, weighting):
        self.__weighting = weighting
    
    def convert_chromosome(self):
        term_x =  str(self.__chromosome[0:4])
        term_y =  str(self.__chromosome[4:8])
        term_w =  str(self.__chromosome[8:12])
        term_z =  str(self.__chromosome[12:16])
        self.__term_x = str(int(term_x, 2)).rjust(2, '0')
        self.__term_y = str(int(term_y, 2)).rjust(2, '0')
        self.__term_w = str(int(term_w, 2)).rjust(2, '0')
        self.__term_z = str(int(term_z, 2)).rjust(2, '0')


class Figure:
    name = None

    def add_area(self, f):
        if isinstance(f, Figure)==False:
            raise ValueError
        return self.area+f.area
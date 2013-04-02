def pre_render(self):
	import pdb; pdb.set_trace()
    for variable in self.variables.items():
        self.variables['static.overlay'] = "enter"

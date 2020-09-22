"""
    def __str__(self):
        r = f'Dominio: {self.dominio}\n'
        r += f'Subdominio: {self.subdom}\n'
        r += f'Paginas: \n'
        for i in self.paginas:
            r += '------\n'
            r += f'{i}'
            r += '\n'
        return r """
        
"""
    def url(self):
        return 'https://wikileaks.org/\n'
    def folder(self):
        return 'News\n'
    def link(self):
        return 'https://wikileaks.org/Amazon-Atlas-Press-Release.html'
    def titulo(self):
        return 'WikiLeaks - Amazon Atlas'
        
"""
class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self.is_turned_on = is_turned_on

    def turn_on(self):
        self.is_turned_on = True
        self._display_image()
    
    def turn_of(self):
        self.is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self.is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
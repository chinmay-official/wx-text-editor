# workingtexteditor.py
import wx

class Menu(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(600, 800))

        # Create the file menu
        menubar = wx.MenuBar()
        file = wx.Menu()

        # Create the file menu item(s)
        new = wx.MenuItem(file, 1, '&New\tCtrl+N')
        open = wx.MenuItem(file, 1, '&Open\tCtrl+O')
        save = wx.MenuItem(file, 1, '&Save\tCtrl+S')
        saveas = wx.MenuItem(file, 1, '&Save as...\tCtrl+Shift+s')
        quit = wx.MenuItem(file, 1, '&Quit\tCtrl+Q')

        file.AppendItem(new)
        file.AppendItem(open)
        file.AppendItem(save)
        file.AppendItem(saveas)
        file.AppendItem(quit)

        self.Bind(wx.EVT_MENU, self.OnNew, id=1)
        self.Bind(wx.EVT_MENU, self.OnOpen, id=1)
        self.Bind(wx.EVT_MENU, self.OnSave, id=1)
        self.Bind(wx.EVT_MENU, self.OnSaveas, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=1)

        menubar.Append(file, '&File')
        self.SetMenuBar(menubar)

        # Create the edit menu
        menubar = wx.MenuBar()
        edit = wx.Menu()

        # Create the edit menu item(s)
        wordwrap = wx.MenuItem(edit, 1, '&Word Wrap\tCtrl+W')
        cut = wx.MenuItem(edit, 1, '&Cut\tCtrl+X')
        copy = wx.MenuItem(edit, 1, '&Copy\tCtrl+C')
        paste = wx.MenuItem(edit, 1, '&Paste\tCtrl+V')

        edit.AppendItem(wordwrap)
        edit.AppendItem(cut)
        edit.AppendItem(copy)
        edit.AppendItem(paste)

        self.Bind(wx.EVT_MENU, self.OnWordWrap, id=1)
        self.Bind(wx.EVT_MENU, self.OnCut, id=1)
        self.Bind(wx.EVT_MENU, self.OnCopy, id=1)
        self.Bind(wx.EVT_MENU, self.OnPaste, id=1)

        menubar.Append(edit, '&Edit')
        self.SetMenuBar(menubar)
        
        # Define the events of the file menu items
    def OnNew(self, event):
        self.New()

    def OnOpen(self, event):
        self.Open()

    def OnSave(self, event):
        self.Save()

    def OnSaveas(self, event):
        self.Saveas()

    def OnQuit(self, event):
        self.Close()

        # Define the events of the edit menu items
    def OnWordWrap(self, event):
        self.WordWrap()

    def OnCut(self, event):
        self.Cut()

    def OnCopy(self, event):
        self.Copy()

    def OnPaste(self, event):
        self.Paste()
        
app = wx.App()
Menu(None, -1, "Stoss' Editor")
app.MainLoop()

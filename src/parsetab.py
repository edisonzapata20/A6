
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CONNECT DISCONNECT NAME SERVER SPACE TOServerAssign_Connection : CONNECT SPACE TO SPACE SERVER SPACE NAME\n                    | DISCONNECT SPACE SERVER NAME\n    '
    
_lr_action_items = {'CONNECT':([0,],[2,]),'DISCONNECT':([0,],[3,]),'$end':([1,9,12,],[0,-2,-1,]),'SPACE':([2,3,6,10,],[4,5,8,11,]),'TO':([4,],[6,]),'SERVER':([5,8,],[7,10,]),'NAME':([7,11,],[9,12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ServerAssign_Connection':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ServerAssign_Connection","S'",1,None,None,None),
  ('ServerAssign_Connection -> CONNECT SPACE TO SPACE SERVER SPACE NAME','ServerAssign_Connection',7,'p_ServerAssign_Connection','parser.py',13),
  ('ServerAssign_Connection -> DISCONNECT SPACE SERVER NAME','ServerAssign_Connection',4,'p_ServerAssign_Connection','parser.py',14),
]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import double_linked_list as dl

#%% Test des fonctions is_empty, insert_first et size_list
print("l=dl.DoubleLinkedList()")
l=dl.DoubleLinkedList()
print("l.is_empty_list():",l.is_empty_list())
for i in range(6,0,-1):
    l.insert_first(i)
print("for i in range(6,0,-1): l.insert_first(i)")
print("print(l):",l)
print("l.size_list():",l.size_list())
print("l.is_empty_list():",l.is_empty_list())

#%% Test de la fonction insert_last
l=dl.DoubleLinkedList()
for i in range(1,7):
    l.insert_last(i)
print("for i in range(1,7): l.insert_last(i)")
print("print(l):",l)

#%% Test des fonctions insert_before, insert_after, insert_at
l=dl.DoubleLinkedList()
for i in range(1,7):
    l.insert_last(i)
print("print(l):",l)
l.insert_before(2.5,3)
print("l.insert_before(2.5,3):",l)
l.insert_before(0.5,1)

print("l.insert_before(0.5,1):",l)
l.insert_after(3.5,3)
print("l.insert_after(3.5,3):",l)
l.insert_after(6.5,6)
print("l.insert_after(6.5,6):",l)
l.insert_at(1.5,1)
print("l.insert_at(1.5,1):",l)



#%% Test des fonctions get_first, get_last, get_at
l=dl.DoubleLinkedList()
for i in range(1,7):
    l.insert_last(i)
print("print(l):",l)
print("l.get_first():",l.get_first())
print("l.get_last():",l.get_last())
print("l.get_at(5):", l.get_at(5))

#%%Test de la fonction delete_at
l=dl.DoubleLinkedList()
for i in range(1,7):
    l.insert_last(i)
print("print(l):",l)
l.delete_at(2)
print("l.delete_at(2):",l)

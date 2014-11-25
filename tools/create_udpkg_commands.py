#!/usr/bin/env python3

# This Script is FAR from complete, and may or may not ever get completed...

# Copyright (C) Jacob J. Walker
#
# The code was influenced by Simon Law's apt-rdepends pearl script
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA


# Note about terminology: 
# This script uses a tree data structure to model dependencies, but
# because a dependency in a package acts like a "biologica" parent, 
# yet is a tree "child".  So for most of this script, the terms
# "child" and "parent" will not be used, and instead the terms
# "dependency" and "derivative" will be used.  But "derivative" 
# does not necessarily mean that it is a legal "derivative work"
# but simply that since it depends upon other packages, it is 
# derived from those packages in some manner.
# Where "child" and "parent" are used, it is based upon tree terminology.


# Import modules / libraries
import sys, apt



# Define tree data structure objects
# ----------------------------------
# Copyright (C) by Brett Kromkamp 2011-2014 (brett@youprogramming.com)
# You Programming (http://www.youprogramming.com)
# May 03, 2014

class Node:
    def __init__(self, identifier):
        self.__identifier = identifier
        self.__children = []

    @property
    def identifier(self):
        return self.__identifier

    @property
    def children(self):
        return self.__children

    def add_child(self, identifier):
        self.__children.append(identifier)


(_ROOT, _DEPTH, _BREADTH) = range(3)


class Tree:

    def __init__(self):
        self.__nodes = {}

    @property
    def nodes(self):
        return self.__nodes

    def add_node(self, identifier, parent=None):
        node = Node(identifier)
        self[identifier] = node

        if parent is not None:
            self[parent].add_child(identifier)

        return node

    def display(self, identifier, depth=_ROOT):
        children = self[identifier].children
        if depth == _ROOT:
            print("{0}".format(identifier))
        else:
            print("t"*depth, "{0}".format(identifier))

        depth += 1
        for child in children:
            self.display(child, depth)  # recursive call

    def traverse(self, identifier, mode=_DEPTH):
        # Python generator. Loosly based on an algorithm from 
        # 'Essential LISP' by John R. Anderson, Albert T. Corbett, 
        # and Brian J. Reiser, page 239-241
        yield identifier
        queue = self[identifier].children
        while queue:
            yield queue[0]
            expansion = self[queue[0]].children
            if mode == _DEPTH:
                queue = expansion + queue[1:]  # depth-first
            elif mode == _BREADTH:
                queue = queue[1:] + expansion  # width-first

    def __getitem__(self, key):
        return self.__nodes[key]

    def __setitem__(self, key, item):
        self.__nodes[key] = item


# Define some "constants"
pcache = apt.Cache()
root_pkg_name = sys.argv[1]
root_pkg = pcache[root_pkg_name]

# Define Functions
# ----------------

def get_depends(derivative_pkg):
  result = []
  base_depends = derivative_pkg.candidate.dependencies
  for count1 in range(len(base_depends)):
    for count2 in range(len(base_depends[count1])):
      result[len(result):] = [pcache[base_depends[count1][count2].name]]

  return result

print(get_depends(root_pkg))

#def get_depends(pkg_name):
#  pkg_cache = apt.Cache()


#  depend_names = [pkg_name]

#  pkg = pkg_cache[pkg_name]
#  dependencies = pkg.candidate.dependencies
#  for count1 in range(len(dependencies)):
#    for count2 in range(len(dependencies[count1])):
#      dependency_names[len(dependency_names):] = [dependencies[count1][count2].name]
#  return dependency_names
  

#print(dependency_names(primary_pkg_name))








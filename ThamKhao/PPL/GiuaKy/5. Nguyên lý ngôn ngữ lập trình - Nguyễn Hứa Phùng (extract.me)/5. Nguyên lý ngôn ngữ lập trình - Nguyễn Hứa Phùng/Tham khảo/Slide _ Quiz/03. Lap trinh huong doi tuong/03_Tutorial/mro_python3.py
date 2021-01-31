class Type(type):
    def __repr__(cls):
        return cls.__name__

class O(object, metaclass=Type): pass

class A(O): pass

class B(A): pass
class D(A): pass
class E(A): pass

class C(B): pass
class G(C,D,E): pass

print(G.mro())

##class A(O): pass
##
##class B(O): pass
##
##class C(O): pass
##
##class D(O): pass
##
##class E(O): pass
##
##class K1(A, B, C): pass # thu tu A B C
##
##class K2(D, B, E): pass
##
##class K3(D, A): pass
##
##class Z(K1, K2, K3): pass
##
##print(Z.mro())


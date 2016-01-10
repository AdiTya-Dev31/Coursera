#include "builtin.hpp"
#include "time.hpp"
#include "copy.hpp"
#include "random.hpp"
#include "math.hpp"
#include "mincut.hpp"

namespace __mincut__ {

str *const_0;


list<str *> *lst;
dict<str *, list<str *> *> *G;
str *__name__, *line;
file::for_in_loop __3;
__iter<str *> *__1;
file *__0, *fin;
__ss_int __2, minelem;



tuple2<str *, str *> *chooseRandomEdge(dict<str *, list<str *> *> *G) {
    str *v1, *v2;

    v1 = (G->keys())->__getfast__(__random__::randint(0, (len(G)-1)));
    v2 = (G->__getitem__(v1))->__getfast__(__random__::randint(0, (len(G->__getitem__(v1))-1)));
    return (new tuple2<str *, str *>(2,v1,v2));
}

void *kargerStep(dict<str *, list<str *> *> *G) {
    list<str *> *__5, *lst;
    tuple2<str *, str *> *__4;
    __iter<str *> *__6;
    list<str *>::for_in_loop __8;
    str *v1, *v2, *x;
    __ss_int __10, __7, __9, i;

    __4 = chooseRandomEdge(G);
    v1 = __4->__getfirst__();
    v2 = __4->__getsecond__();
    (G->__getitem__(v1))->extend(G->__getitem__(v2));

    FOR_IN(x,G->__getitem__(v2),5,7,8)
        lst = G->__getitem__(x);

        FAST_FOR(i,0,len(lst),1,9,10)
            if (__eq(lst->__getfast__(i), v2)) {
                lst->__setitem__(i, v1);
            }
        END_FOR

    END_FOR


    while ((G->__getitem__(v1))->__contains__(v1)) {
        (G->__getitem__(v1))->remove(v1);
    }
    G->__delitem__(v2);
    return NULL;
}

__ss_int karger(dict<str *, list<str *> *> *G) {
    

    while ((len(G)>2)) {
        kargerStep(G);
    }
    return len(G->__getitem__((G->keys())->__getfast__(0)));
}

void __init() {
    const_0 = new str("kargerMinCut.txt");

    __name__ = new str("__main__");

    fin = open(const_0);
    G = (new dict<str *, list<str *> *>());

    FOR_IN(line,fin,0,2,3)
        lst = (new list<str *>());
        lst = line->split();
        G->__setitem__(lst->__getfast__(0), lst->__slice__(1, 1, 0, 0));
    END_FOR

    minelem = karger(__copy__::deepcopy(G));
    print2(NULL,0,1, ___box(minelem));
}

} // module namespace

int main(int, char **) {
    __shedskin__::__init();
    __math__::__init();
    __time__::__init();
    __random__::__init();
    __copy__::__init();
    __shedskin__::__start(__mincut__::__init);
}

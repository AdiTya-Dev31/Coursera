#ifndef __MINCUT_HPP
#define __MINCUT_HPP

using namespace __shedskin__;
namespace __mincut__ {

extern str *const_0;



extern __ss_int __2, minelem;
extern dict<str *, list<str *> *> *G;
extern str *__name__, *line;
extern list<str *> *lst;
extern __iter<str *> *__1;
extern file *__0, *fin;


tuple2<str *, str *> *chooseRandomEdge(dict<str *, list<str *> *> *G);
void *kargerStep(dict<str *, list<str *> *> *G);
__ss_int karger(dict<str *, list<str *> *> *G);

} // module namespace
#endif

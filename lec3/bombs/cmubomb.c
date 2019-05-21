#include <stdio.h>

typedef struct node {
    int val;
    int id;
    int next;
} node

int main() {
    int i = 0;				// $edi
    int* iarr = {1, 2, 3, 4, 5, 6};	// $ecx = [local_18h]
    
    node nodelist;			// local_30h
    node* nodelist = &nodelist;		// local_3ch

    node node6;
    node6.val  = 0x01b0;
    node6.id   = 0x06;
    node6.next = 0x00;

    node node5;
    node5.val  = 0xd4;
    node5.id   = 0x05;
    node5.next = node6;

    node node4;
    node4.val  = 0x03e5;
    node4.id   = 0x04;
    node4.next = node5;

    node node3;
    node3.val  = 0x012d;
    node3.id   = 0x03;
    node3.next = node4;

    node node2;
    node2.val  = 0x02d5;
    node2.id   = 0x02;
    node2.next = node3;

    node node1;
    node1.val  = 0xfd;
    node1.id   = 0x01;
    node1.next = node2;

    node* cnode = &node1;		// esi -- local_34h

    do {
        int j = 1			// $ebx
        $edx = i * 4
        if (1 < iarr[i]) {
            $eax = iarr[i]
            do {
                cnode = cnode.next;
                j += 1;
            } while (j < iarr[i]);
        }
        $edx = unknownp;
        unknownp[i] = carr;
        i++;
    } while(i <= 5);


    cnode = nodelist;
    i = 1;
    do {
        $eax = cnode[i];
        nodelist[0].next = cnode[i];
        $esi = $eax;
        i++;
    while (i <= 5);

    return 0;
}


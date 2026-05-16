# Linked List

A linked list is a data structure consisting of a sequence of nodes, where each node is linked to the next. A node in a linked list has two main components: the data it stores (val) and a reference to the next node (next) in the sequence.

### Singly linked list

- Simplest form of linked list.
- Each node points to the next node in the linked list.
- The last node points to nothing (null).
- The start is called head.
- To access other nodes we need to traverse it starting at the head.
- Can be used to store a collection of data.
- Dynamic sizing capability: they can grow or shrink in size flexibly.
- Excel in scenarios requiring frequent insertions and deletions.

### Doubly linked list

- Extended version of the linked list
- Each node contains two references: one to the next node (next), and one to the previous node (prev).
- Usually have immediate access to both the head node and the tail node.
- Allows bidirectional traversal.
- Deletions generally are more straightforward.

---

### Real-World Example

Music Playlist: Music player applications often use linked lists to implement playlists, particularly doubly linked lists, where each song node links to the next and previous songs. This structure enables efficient addition, removal, and reordering of songs because only the pointers between nodes need to be updated, rather than moving the song data in memory.

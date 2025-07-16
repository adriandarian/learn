// Definition for singly-linked list.
function ListNode(val) {
  this.val = val;
  this.next = null;
}

/**
 * @param {ListNode} listOne
 * @param {ListNode} listTwo
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let combined = 0,
    placeholder = null,
    i = 0,
    result,
    curr;

  while (l1 || l2) {
    // Adds the current index of each together if a value exists or defaults value to 0
    combined = (l1 ? l1.val : 0) + (l2 ? l2.val : 0);

    // Iterates l1 to next node
    if (l1) {
      l1 = l1.next;
    }

    // Iterates l2 to next node
    if (l2) {
      l2 = l2.next;
    }

    // Adds previous placeholder if one exists to the current value
    if (placeholder) {
      combined += placeholder;
      placeholder = null;
    }

    // Splits two digit value into 2 variables (one global and one scoped)
    if (combined > 9) {
      placeholder = +combined.toString()[0];
      combined = +combined.toString()[1];
    }

    // Creates head node if not already created otherwise appends next node
    if (i === 0) {
      result = new ListNode(combined);
      curr = result;
      i++;
    } else {
      curr.next = new ListNode(combined);
      curr = curr.next;
    }
  }

  // Append extra node if last computation returned a two digit number
  curr.next = placeholder ? new ListNode(placeholder) : null;

  return result;
};

addTwoNumbers([2, 4, 3], [5, 6, 4]);

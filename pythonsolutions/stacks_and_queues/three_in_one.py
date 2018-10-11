class MultiStack:
    """An implementation of n stacks using a single array

    Elements are interleaved in a single array. For example, if there are 3
    stacks, index 0 belongs to stack 0, index 1 belongs to stack 1, index 2
    belongs to stack 2, index 3 belongs to stack 0, etc.

    This means that shifting elements is not necessary although there is more
    wasted space if stack lengths are uneven. However, we still have to allocate
    a new array whenever we extend the list so the only benefit of this strategy
    is the ease of implementation.
    """
    def __init__(self, num_stacks: int = 3):
        self._array = [None for _ in range(num_stacks)]
        self._stack_lens = [0 for _ in range(num_stacks)]
        self.num_stacks = num_stacks

    def _prev_idx(self, stack_id: int) -> int:
        """Get index of last element in a stack

        Args:
            stack_id:

        Returns:
            index of last element in a stack
        """
        return (self._stack_lens[stack_id] - 1) * self.num_stacks + stack_id

    def _next_idx(self, stack_id: int) -> int:
        """Get index of next element in a stack

        Args:
            stack_id: a stack ID

        Returns:
            index of next element in a stack
        """
        return self._stack_lens[stack_id] * self.num_stacks + stack_id

    def push(self, value: object, stack_id: int) -> None:
        """Push a value onto a stack

        Args:
            value: value to push
            stack_id: stack to push to (0 indexed)

        Returns:
            None
        """
        idx = self._next_idx(stack_id)
        try:
            self._array[idx] = value
        except IndexError:
            self._array.extend(None for _ in range(len(self._array)))
            self._array[idx] = value
        self._stack_lens[stack_id] += 1

    def pop(self, stack_id: int) -> object:
        """Pop a value from a stack

        Args:
            stack_id: stack to pop from

        Returns:
            last value in the stack
        """
        if self._stack_lens[stack_id] > 0:
            idx = self._next_idx(stack_id) - self.num_stacks
            val = self._array[idx]
            self._stack_lens[stack_id] -= 1
            return val
        else:
            raise IndexError(f'stack {stack_id} is empty')

    def peek(self, stack_id: int) -> object:
        """Look at the last value on a stack

        Args:
            stack_id: stack to look at

        Returns:
            last value in the stack
        """
        if self._stack_lens[stack_id] > 0:
            idx = self._next_idx(stack_id) - self.num_stacks
            return self._array[idx]
        else:
            raise IndexError(f'stack {stack_id} is empty')

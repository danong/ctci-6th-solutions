class MultiStack:
    def __init__(self, num_stacks: int = 3):
        self._array = [None for _ in range(num_stacks)]
        self._stack_lens = [0 for _ in range(num_stacks)]
        self.num_stacks = num_stacks

    def _prev_idx(self, stack_id: int) -> int:
        return (self._stack_lens[stack_id] - 1) * self.num_stacks + stack_id

    def _next_idx(self, stack_id):
        return self._stack_lens[stack_id] * self.num_stacks + stack_id

    def push(self, value: object, stack_id: int) -> None:
        idx = self._next_idx(stack_id)
        try:
            self._array[idx] = value
        except IndexError:
            self._array.extend(None for _ in range(len(self._array)))
            self._array[idx] = value
        self._stack_lens[stack_id] += 1

    def pop(self, stack_id: int) -> object:
        if self._stack_lens[stack_id] > 0:
            idx = self._next_idx(stack_id) - self.num_stacks
            val = self._array[idx]
            self._stack_lens[stack_id] -= 1
            return val
        else:
            raise IndexError('pop from empty list')

    def peek(self, stack_id: int) -> object:
        if self._stack_lens[stack_id] > 0:
            idx = self._next_idx(stack_id) - self.num_stacks
            return self._array[idx]
        else:
            raise IndexError('pop from empty list')

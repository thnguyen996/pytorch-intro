# Tensor and operations

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #                       __________________________________ 
    #                      < “Do you know what a Tensor is? ” >
    #                       ---------------------------------- 
    #                              \   ^__^
    #                               \  (oo)\_______
    #                                  (__)\       )\/\
    #                                      ||----w |
    #                                      ||     ||

    #%%

---

## What is a tensor in pytorch?

- Pytorch uses tensor to do all operation

- ‘A tensor’ is a “multi-dimention matrix” (Simillar to ndarray in ‘numpy’)

---

## Let’s create a tensor:

### Import Pytorch and set manual seed:

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Create a tensor:

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Empty tensor, random tensor, constant values:

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Attributes of a Tensor:

    - shape, reshape

    - dtype

    - device

    - requires_grad

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Convert tensor to np array and back:

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Standard numpy-like indexing and slicing:

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Arithmetic operation on tensors:

    - add

    - mul

    - sub

    - div

    - inplace operations

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Excercise:

    - Create 2 (3, 3, 3) tensors with dtype is float64 and add them together and print out the results

### Solution:

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%
    tensor1 = torch.randn(3, 3, 3, dtype = torch.float64)
    tensor2 = torch.randn(3, 3, 3, dtype = torch.float64)
    sum_tensor = torch.add(tensor1, tensor2)
    print(sum_tensor)

          #%%

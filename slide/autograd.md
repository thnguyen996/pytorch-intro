# Pytorch autograd

**Automatic differentiation with torch.autograd:**

    - Use to automatically compute the gradient of a tensor

## Pytorch autograd:

### Create tensor with requires_grad=True and compute gradient (random seed):

    - create tensor x

    - y = mean(2x), grad_fn

    - calculate gradient dy/dx

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Remember to clear your gradient:

    - Pytorch automatically accumulate the gradient → Need to clear before update weight

    - Use ‘tensor.grad.zero_()’

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Exercise:

Given 2 (2, 2) random tensors a and b and a function ‘f(a, b) = sum(3*a**3 - b**2)’. Compute gradien of f w.r.t a and b.

### Solution:

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%
    a = torch.randn(2, 2, requires_grad=True)
    b = torch.randn(2, 2, requires_grad=True)

    f = 3*a**3 - b**2
    f.sum().backward()
    print("Gradient of f w.r.t a is: ", a.grad )
    print("Gradient of f w.r.t b is: ", b.grad)
       #%%

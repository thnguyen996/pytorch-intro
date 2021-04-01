# Simple example

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%
       #       ________________________________________________       
       #      < “Let’s build a simple Linear Regression model” >
       #       ------------------------------------------------
       #              \   ^__^
       #               \  (oo)\_______
       #                  (__)\       )\/\
       #                      ||----w |
       #                      ||     ||
       #
       #                         * * *

    #%%

## Step that we need:

    1. Load the dataset

    2. Build the model

    3. Define loss function and optimizer

    4. Train the model

    5. Evaluate the model

### Load dummy dataset

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%
    x_train = torch.tensor([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168],
                        [9.779], [6.182], [7.59], [2.167], [7.042],
                        [10.791], [5.313], [7.997], [3.1]], dtype=torch.float32, requires_grad=True)

    y_train = torch.tensor([[1.7], [2.76], [2.09], [3.19], [1.694], [1.573],
                        [3.366], [2.596], [2.53], [1.221], [2.827],
                        [3.465], [1.65], [2.904], [1.3]], dtype=torch.float32, requires_grad=True)

    print(x_train.shape, y_train.shape)
    #%%

### Linear regression model

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Loss and optimizer

    - Use Mean Square Error Loss and Stochastic Gradient decent algo.

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Train the model

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

### Evaluation

    - Plot the data (import matplotlib.pyplot as plt, mpld3)

    - Save the model using torch.save()

<!-- An innocent comment to force Markdown out of list parsing mode. See also http://meta.stackoverflow.com/a/99637 -->

    #%%

    #%%

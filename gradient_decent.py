#! usr/bin/env python

def gradient_descent(alpha, x, y, ep=0.0001, max_iter=100000):
    converged = False
    iter = 0
    m = len(x) # number of samples

    # initial theta
    t0 = 10
    t1 = 10
    # t0 = np.random.random(x.shape[1])
    # t1 = np.random.random(x.shape[1])

    # total error, J(theta)
    J = sum([(t0 + t1*x[i] - y[i])**2 for i in range(m)])

    # Iterate Loop
    while not converged:
        # for each training sample, compute the gradient (d/d_theta j(theta))
        grad0 = 1.0/m * sum([(t0 + t1*x[i] - y[i]) for i in range(m)])
        grad1 = 1.0/m * sum([(t0 + t1*x[i] - y[i])*x[i] for i in range(m)])

        # update the theta_temp
        temp0 = t0 - alpha * grad0
        temp1 = t1 - alpha * grad1

        # update theta
        t0 = temp0
        t1 = temp1

        # mean squared error
        e = sum( [ (t0 + t1*x[i] - y[i])**2 for i in range(m)] )

        if abs(J-e) <= ep:
            print 'Converged, iterations: ', iter
            converged = True

        J = e   # update error
        iter += 1  # update iter

        if iter == max_iter:
            print 'Max interactions exceeded!'
            converged = True

    return t0,t1

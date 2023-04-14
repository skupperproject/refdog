    #
    # Current
    #
    skupper service create backend 8080
    skupper service bind backend deployment/backend --target-port 9090
    #
    # Proposed (general purpose form)
    #
    skupper provided-service create backend deployment/backend
    skupper provided-service create-port backend 8080 --target-port 9090
    #
    # Proposed (simplified form for the common case)
    #
    skupper provide backend:8080 deployment/backend --target-port 9090


    skupper required-service create-port backend 8080
    #
    # Proposed (simplified form for the common case)
    #
    skupper require backend:8080

import numpy as np

def extract_rigid_transformation(X, Y):
    """
    Extracts the rigid transformation (rotation, translation, and scale)
    from the Procrustes-aligned shape.

    Parameters:
    - X: Original shape (N x 3), each row is a 3D point.
    - Y: Aligned shape (N x 3), each row is a 3D point.

    Returns:
    - R: Rotation matrix (3x3)
    - s: Scale factor (scalar)
    - t: Translation vector (3,)
    """
    # Compute centroids
    X_mean = np.mean(X, axis=0)
    Y_mean = np.mean(Y, axis=0)

    # Center the points
    X_centered = X - X_mean
    Y_centered = Y - Y_mean

    # Compute the covariance matrix
    H = X_centered.T @ Y_centered

    # Compute Singular Value Decomposition (SVD)
    U, S, Vt = np.linalg.svd(H)

    # Compute rotation matrix
    R = Vt.T @ U.T

    # Ensure a proper rotation (det(R) = 1, not a reflection)
    if np.linalg.det(R) < 0:
        Vt[-1, :] *= -1
        R = Vt.T @ U.T

    # Compute scale
    # s = np.sum(S) / np.sum(X_centered ** 2)

    # Compute translation
    t = Y_mean - R @ X_mean

    return R, t

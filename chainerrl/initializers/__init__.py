from chainerrl.initializers.constant import VarianceScalingConstant  # NOQA

# LeCunNormal was merged into Chainer v3, thus removed from ChainerRL.
# For backward compatibility, it is still imported in this namespace.
from chainer.initializers import LeCunNormal  # NOQA

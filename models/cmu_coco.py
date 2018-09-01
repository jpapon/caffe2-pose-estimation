"""Model definition. """

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

def gauss_fill(std):
    """Gaussian fill helper to reduce verbosity."""
    return ('GaussianFill', {'std': std})

def const_fill(value):
    """Constant fill helper to reduce verbosity."""
    return ('ConstantFill', {'value': value})

def cmu_coco(model): # original cmu coco iter440000 model
    model.Conv('data', 'conv1_1', 3, 64, 3, pad=1, stride=1)
    model.Relu('conv1_1', 'conv1_1')
    model.Conv('conv1_1', 'conv1_2', 64, 64, 3, pad=1, stride=1)
    model.Relu('conv1_2', 'conv1_2')
    model.MaxPool('conv1_2', 'pool1_stage1', kernel=2, pad=0, stride=2)
    model.Conv('pool1_stage1', 'conv2_1', 64, 128, 3, pad=1, stride=1)
    model.Relu('conv2_1', 'conv2_1')
    model.Conv('conv2_1', 'conv2_2', 128, 128, 3, pad=1, stride=1)
    model.Relu('conv2_2', 'conv2_2')
    model.MaxPool('conv2_2', 'pool2_stage1', kernel=2, pad=0, stride=2)
    model.Conv('pool2_stage1', 'conv3_1', 128, 256, 3, pad=1, stride=1)
    model.Relu('conv3_1', 'conv3_1')
    model.Conv('conv3_1', 'conv3_2', 256, 256, 3, pad=1, stride=1)
    model.Relu('conv3_2', 'conv3_2')
    model.Conv('conv3_2', 'conv3_3', 256, 256, 3, pad=1, stride=1)
    model.Relu('conv3_3', 'conv3_3')
    model.Conv('conv3_3', 'conv3_4', 256, 256, 3, pad=1, stride=1)
    model.Relu('conv3_4', 'conv3_4')
    model.MaxPool('conv3_4', 'pool3_stage1', kernel=2, pad=0, stride=2)
    model.Conv('pool3_stage1', 'conv4_1', 256, 512, 3, pad=1, stride=1)
    model.Relu('conv4_1', 'conv4_1')
    model.Conv('conv4_1', 'conv4_2', 512, 512, 3, pad=1, stride=1)
    model.Relu('conv4_2', 'conv4_2')
    model.Conv('conv4_2', 'conv4_3_CPM', 512, 256, 3, pad=1, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('conv4_3_CPM', 'conv4_3_CPM')
    model.Conv('conv4_3_CPM', 'conv4_4_CPM', 256, 128, 3, pad=1, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('conv4_4_CPM', 'conv4_4_CPM')
    # limb
    model.Conv('conv4_4_CPM', 'conv5_1_CPM_L1', 128, 128, 3, pad=1, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('conv5_1_CPM_L1', 'conv5_1_CPM_L1')
    model.Conv('conv5_1_CPM_L1', 'conv5_2_CPM_L1', 128, 128, 3, pad=1, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('conv5_2_CPM_L1', 'conv5_2_CPM_L1')
    model.Conv('conv5_2_CPM_L1', 'conv5_3_CPM_L1', 128, 128, 3, pad=1, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('conv5_3_CPM_L1', 'conv5_3_CPM_L1')
    model.Conv('conv5_3_CPM_L1', 'conv5_4_CPM_L1', 128, 512, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('conv5_4_CPM_L1', 'conv5_4_CPM_L1')
    model.Conv('conv5_4_CPM_L1', 'conv5_5_CPM_L1', 512, 38, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    # joint
    model.Conv('conv4_4_CPM', 'conv5_1_CPM_L2', 128, 128, 3, pad=1, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('conv5_1_CPM_L2', 'conv5_1_CPM_L2')
    model.Conv('conv5_1_CPM_L2', 'conv5_2_CPM_L2', 128, 128, 3, pad=1, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('conv5_2_CPM_L2', 'conv5_2_CPM_L2')
    model.Conv('conv5_2_CPM_L2', 'conv5_3_CPM_L2', 128, 128, 3, pad=1, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('conv5_3_CPM_L2', 'conv5_3_CPM_L2')
    model.Conv('conv5_3_CPM_L2', 'conv5_4_CPM_L2', 128, 512, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('conv5_4_CPM_L2', 'conv5_4_CPM_L2')
    model.Conv('conv5_4_CPM_L2', 'conv5_5_CPM_L2', 512, 19, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    # concat
    model.Concat(['conv5_5_CPM_L1', 'conv5_5_CPM_L2', 'conv4_4_CPM'], 'concat_stage2')
    # refinement 1 - limb
    model.Conv('concat_stage2', 'Mconv1_stage2_L1', 185, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv1_stage2_L1', 'Mconv1_stage2_L1')
    model.Conv('Mconv1_stage2_L1', 'Mconv2_stage2_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv2_stage2_L1', 'Mconv2_stage2_L1')
    model.Conv('Mconv2_stage2_L1', 'Mconv3_stage2_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv3_stage2_L1', 'Mconv3_stage2_L1')
    model.Conv('Mconv3_stage2_L1', 'Mconv4_stage2_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv4_stage2_L1', 'Mconv4_stage2_L1')
    model.Conv('Mconv4_stage2_L1', 'Mconv5_stage2_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv5_stage2_L1', 'Mconv5_stage2_L1')
    model.Conv('Mconv5_stage2_L1', 'Mconv6_stage2_L1', 128, 128, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv6_stage2_L1', 'Mconv6_stage2_L1')
    model.Conv('Mconv6_stage2_L1', 'Mconv7_stage2_L1', 128, 38, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    # refinement 1 - joint
    model.Conv('concat_stage2', 'Mconv1_stage2_L2', 185, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv1_stage2_L2', 'Mconv1_stage2_L2')
    model.Conv('Mconv1_stage2_L2', 'Mconv2_stage2_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv2_stage2_L2', 'Mconv2_stage2_L2')
    model.Conv('Mconv2_stage2_L2', 'Mconv3_stage2_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv3_stage2_L2', 'Mconv3_stage2_L2')
    model.Conv('Mconv3_stage2_L2', 'Mconv4_stage2_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv4_stage2_L2', 'Mconv4_stage2_L2')
    model.Conv('Mconv4_stage2_L2', 'Mconv5_stage2_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv5_stage2_L2', 'Mconv5_stage2_L2')
    model.Conv('Mconv5_stage2_L2', 'Mconv6_stage2_L2', 128, 128, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv6_stage2_L2', 'Mconv6_stage2_L2')
    model.Conv('Mconv6_stage2_L2', 'Mconv7_stage2_L2', 128, 19, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    # concat3
    model.Concat(['Mconv7_stage2_L1', 'Mconv7_stage2_L2', 'conv4_4_CPM'], 'concat_stage3')
    # refinement 2 - limb
    model.Conv('concat_stage3', 'Mconv1_stage3_L1', 185, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv1_stage3_L1', 'Mconv1_stage3_L1')
    model.Conv('Mconv1_stage3_L1', 'Mconv2_stage3_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv2_stage3_L1', 'Mconv2_stage3_L1')
    model.Conv('Mconv2_stage3_L1', 'Mconv3_stage3_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv3_stage3_L1', 'Mconv3_stage3_L1')
    model.Conv('Mconv3_stage3_L1', 'Mconv4_stage3_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv4_stage3_L1', 'Mconv4_stage3_L1')
    model.Conv('Mconv4_stage3_L1', 'Mconv5_stage3_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv5_stage3_L1', 'Mconv5_stage3_L1')
    model.Conv('Mconv5_stage3_L1', 'Mconv6_stage3_L1', 128, 128, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv6_stage3_L1', 'Mconv6_stage3_L1')
    model.Conv('Mconv6_stage3_L1', 'Mconv7_stage3_L1', 128, 38, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    # refinement 2 - joint
    model.Conv('concat_stage3', 'Mconv1_stage3_L2', 185, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv1_stage3_L2', 'Mconv1_stage3_L2')
    model.Conv('Mconv1_stage3_L2', 'Mconv2_stage3_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv2_stage3_L2', 'Mconv2_stage3_L2')
    model.Conv('Mconv2_stage3_L2', 'Mconv3_stage3_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv3_stage3_L2', 'Mconv3_stage3_L2')
    model.Conv('Mconv3_stage3_L2', 'Mconv4_stage3_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv4_stage3_L2', 'Mconv4_stage3_L2')
    model.Conv('Mconv4_stage3_L2', 'Mconv5_stage3_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv5_stage3_L2', 'Mconv5_stage3_L2')
    model.Conv('Mconv5_stage3_L2', 'Mconv6_stage3_L2', 128, 128, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv6_stage3_L2', 'Mconv6_stage3_L2')
    model.Conv('Mconv6_stage3_L2', 'Mconv7_stage3_L2', 128, 19, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    # concat4
    model.Concat(['Mconv7_stage3_L1', 'Mconv7_stage3_L2', 'conv4_4_CPM'], 'concat_stage4')
    # refinement 2 - limb
    model.Conv('concat_stage4', 'Mconv1_stage4_L1', 185, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv1_stage4_L1', 'Mconv1_stage4_L1')
    model.Conv('Mconv1_stage4_L1', 'Mconv2_stage4_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv2_stage4_L1', 'Mconv2_stage4_L1')
    model.Conv('Mconv2_stage4_L1', 'Mconv3_stage4_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv3_stage4_L1', 'Mconv3_stage4_L1')
    model.Conv('Mconv3_stage4_L1', 'Mconv4_stage4_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv4_stage4_L1', 'Mconv4_stage4_L1')
    model.Conv('Mconv4_stage4_L1', 'Mconv5_stage4_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv5_stage4_L1', 'Mconv5_stage4_L1')
    model.Conv('Mconv5_stage4_L1', 'Mconv6_stage4_L1', 128, 128, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv6_stage4_L1', 'Mconv6_stage4_L1')
    model.Conv('Mconv6_stage4_L1', 'Mconv7_stage4_L1', 128, 38, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    # refinement 2 - joint
    model.Conv('concat_stage4', 'Mconv1_stage4_L2', 185, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv1_stage4_L2', 'Mconv1_stage4_L2')
    model.Conv('Mconv1_stage4_L2', 'Mconv2_stage4_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv2_stage4_L2', 'Mconv2_stage4_L2')
    model.Conv('Mconv2_stage4_L2', 'Mconv3_stage4_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv3_stage4_L2', 'Mconv3_stage4_L2')
    model.Conv('Mconv3_stage4_L2', 'Mconv4_stage4_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv4_stage4_L2', 'Mconv4_stage4_L2')
    model.Conv('Mconv4_stage4_L2', 'Mconv5_stage4_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv5_stage4_L2', 'Mconv5_stage4_L2')
    model.Conv('Mconv5_stage4_L2', 'Mconv6_stage4_L2', 128, 128, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv6_stage4_L2', 'Mconv6_stage4_L2')
    model.Conv('Mconv6_stage4_L2', 'Mconv7_stage4_L2', 128, 19, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    # concat5
    model.Concat(['Mconv7_stage4_L1', 'Mconv7_stage4_L2', 'conv4_4_CPM'], 'concat_stage5')
    # refinement 2 - limb
    model.Conv('concat_stage5', 'Mconv1_stage5_L1', 185, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv1_stage5_L1', 'Mconv1_stage5_L1')
    model.Conv('Mconv1_stage5_L1', 'Mconv2_stage5_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv2_stage5_L1', 'Mconv2_stage5_L1')
    model.Conv('Mconv2_stage5_L1', 'Mconv3_stage5_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv3_stage5_L1', 'Mconv3_stage5_L1')
    model.Conv('Mconv3_stage5_L1', 'Mconv4_stage5_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv4_stage5_L1', 'Mconv4_stage5_L1')
    model.Conv('Mconv4_stage5_L1', 'Mconv5_stage5_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv5_stage5_L1', 'Mconv5_stage5_L1')
    model.Conv('Mconv5_stage5_L1', 'Mconv6_stage5_L1', 128, 128, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv6_stage5_L1', 'Mconv6_stage5_L1')
    model.Conv('Mconv6_stage5_L1', 'Mconv7_stage5_L1', 128, 38, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    # refinement 2 - joint
    model.Conv('concat_stage5', 'Mconv1_stage5_L2', 185, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv1_stage5_L2', 'Mconv1_stage5_L2')
    model.Conv('Mconv1_stage5_L2', 'Mconv2_stage5_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv2_stage5_L2', 'Mconv2_stage5_L2')
    model.Conv('Mconv2_stage5_L2', 'Mconv3_stage5_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv3_stage5_L2', 'Mconv3_stage5_L2')
    model.Conv('Mconv3_stage5_L2', 'Mconv4_stage5_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv4_stage5_L2', 'Mconv4_stage5_L2')
    model.Conv('Mconv4_stage5_L2', 'Mconv5_stage5_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv5_stage5_L2', 'Mconv5_stage5_L2')
    model.Conv('Mconv5_stage5_L2', 'Mconv6_stage5_L2', 128, 128, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv6_stage5_L2', 'Mconv6_stage5_L2')
    model.Conv('Mconv6_stage5_L2', 'Mconv7_stage5_L2', 128, 19, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    # concat6
    model.Concat(['Mconv7_stage5_L1', 'Mconv7_stage5_L2', 'conv4_4_CPM'], 'concat_stage6')
    # refinement 2 - limb
    model.Conv('concat_stage6', 'Mconv1_stage6_L1', 185, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv1_stage6_L1', 'Mconv1_stage6_L1')
    model.Conv('Mconv1_stage6_L1', 'Mconv2_stage6_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv2_stage6_L1', 'Mconv2_stage6_L1')
    model.Conv('Mconv2_stage6_L1', 'Mconv3_stage6_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv3_stage6_L1', 'Mconv3_stage6_L1')
    model.Conv('Mconv3_stage6_L1', 'Mconv4_stage6_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv4_stage6_L1', 'Mconv4_stage6_L1')
    model.Conv('Mconv4_stage6_L1', 'Mconv5_stage6_L1', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv5_stage6_L1', 'Mconv5_stage6_L1')
    model.Conv('Mconv5_stage6_L1', 'Mconv6_stage6_L1', 128, 128, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv6_stage6_L1', 'Mconv6_stage6_L1')
    blob_out_limb=model.Conv('Mconv6_stage6_L1', 'Mconv7_stage6_L1', 128, 38, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    # refinement 2 - joint
    model.Conv('concat_stage6', 'Mconv1_stage6_L2', 185, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv1_stage6_L2', 'Mconv1_stage6_L2')
    model.Conv('Mconv1_stage6_L2', 'Mconv2_stage6_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv2_stage6_L2', 'Mconv2_stage6_L2')
    model.Conv('Mconv2_stage6_L2', 'Mconv3_stage6_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv3_stage6_L2', 'Mconv3_stage6_L2')
    model.Conv('Mconv3_stage6_L2', 'Mconv4_stage6_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv4_stage6_L2', 'Mconv4_stage6_L2')
    model.Conv('Mconv4_stage6_L2', 'Mconv5_stage6_L2', 128, 128, 7, pad=3, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv5_stage6_L2', 'Mconv5_stage6_L2')
    model.Conv('Mconv5_stage6_L2', 'Mconv6_stage6_L2', 128, 128, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    model.Relu('Mconv6_stage6_L2', 'Mconv6_stage6_L2')
    blob_out_joint=model.Conv('Mconv6_stage6_L2', 'Mconv7_stage6_L2', 128, 19, 1, pad=0, stride=1, weight_init=gauss_fill(0.01), bias_init=const_fill(0.0))
    return blob_out_limb, blob_out_joint
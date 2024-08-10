import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('../[7] Neural_Nets/Clothing_Classification/xception_v4_large_04_0.880.keras')

# Новый формат для сохранения SavedModel
model.export('../[9] Kuberflow/clothing-model')

'''
BASH:
saved_model_cli show --dir clothing-model --all


signature_def['__saved_model_init_op']:
  The given SavedModel SignatureDef contains the following input(s):
  The given SavedModel SignatureDef contains the following output(s):
    outputs['__saved_model_init_op'] tensor_info:
        dtype: DT_INVALID
        shape: unknown_rank
        name: NoOp
  Method name is: 

signature_def['serve']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['input_layer_34'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 299, 299, 3)
        name: serve_input_layer_34:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['output_0'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 10)
        name: StatefulPartitionedCall:0
  Method name is: tensorflow/serving/predict

signature_def['serving_default']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['input_layer_34'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 299, 299, 3)
        name: serving_default_input_layer_34:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['output_0'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 10)
        name: StatefulPartitionedCall_1:0
  Method name is: tensorflow/serving/predict
The MetaGraph with tag set ['serve'] contains the following ops: {'MergeV2Checkpoints', 'DisableCopyOnRead', 'Placeholder', 'DepthwiseConv2dNative', 'StringJoin', 'ReadVariableOp', 'Select', 'Pack', 'VarHandleOp', 'Identity', 'StatefulPartitionedCall', 'Const', 'ShardedFilename', 'MatMul', 'AddV2', 'Rsqrt', 'Mean', 'VarIsInitializedOp', 'Conv2D', 'Sub', 'SaveV2', 'Mul', 'AssignVariableOp', 'StaticRegexFullMatch', 'NoOp', 'MaxPool', 'RestoreV2', 'Relu'}

Concrete Functions:
  Function Name: 'serve'
    Option #1
      Callable with:
        Argument #1
          input_layer_34: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='input_layer_34')


'''
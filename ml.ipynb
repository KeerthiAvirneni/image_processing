{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#data loader\n",
    "#this will prepare training data for model\n",
    "\n",
    "import tensorflow as tf\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tensorflow.python.ops import array_ops, math_ops"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#training the data\n",
    "class dataloader(object):\n",
    "    def __init__(self,image_dir,hr_image_size):\n",
    "        self.image_paths = [os.path.jain(image_dir,x)for x in os.listdir(image_dir)]\n",
    "        self.image_size=hr_image_size\n",
    "#parse helps converting image to the machine understanding form\n",
    "    def __parse_image(self,image_path):\n",
    "        image = tf.io.read_file(image_path)\n",
    "        image = tf.io.decode_jepg(image,channels=3)\n",
    "        image = tf.image.conver_image_dtype(image,tf.float32)\n",
    "        \n",
    "        if tf.kerasbackend.image_data_format() == 'channels_last':\n",
    "            shape= array_ops.shape(image)[:2]\n",
    "        else:\n",
    "            shape = array_ops_shape(image)[1:]\n",
    "        cond = math_ops.reduce_all(shape >= tf.constant(self,image_size))\n",
    "        \n",
    "        image = tf.cond(cond,lambda: tf.identity(image)),lambda: tf.image.resize(image,[self.image_size,self.image_size])\n",
    "        \n",
    "        return image\n",
    "    #random crop helps to randomly crop the image and helps in increase in accuracy in conversion\n",
    "    def _random_crop(self,image):\n",
    "        \n",
    "        low_res =tf.image.randon_crop(image,[self.image_size,self.image_size,3])\n",
    "        return image\n",
    "    def _high_low_res_pairs(self , high_res):\n",
    "        \n",
    "        low_res=tf.image.resize(high_res, [self.image_size//4,self.image_size//4],method='bicubic')\n",
    "        return low_res,high_res\n",
    "    #rescale helps to zoom and unzoom the image for finding accuracy\n",
    "    def _rescale(self , low_res,high_res):\n",
    "        high_res = high_res * 2.0-1.0\n",
    "        return low_res , high_res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

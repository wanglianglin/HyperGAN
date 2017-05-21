import tensorflow as tf
import hyperchamber as hc
import numpy as np
from hypergan.discriminators.pyramid_discriminator import PyramidDiscriminator
from hypergan.ops import TensorflowOps

from unittest.mock import MagicMock

from hypergan.trainers.proportional_control_trainer import ProportionalControlTrainer

trainer = ProportionalControlTrainer()
class ProportionalControlTrainerTest(tf.test.TestCase):
    def testConfig(self):
        with self.test_session():
            self.assertEqual(trainer.config.d_learn_rate, 1e-3)

    def testStep(self):
        with self.test_session():
            self.assertEqual(trainer.step(), [1, 1])

if __name__ == "__main__":
    tf.test.main()
